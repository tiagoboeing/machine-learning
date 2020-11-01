import warnings
from keras import optimizers
from keras import layers
from keras import models
import keras
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import json
from config import IS_DEBUG
from logger import Logger
import csv
import pathlib
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import librosa
import sys
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Preprocessing

# Keras

# Logging
warnings.filterwarnings('ignore')


class ClassifyAudio():
    def __init__(self, create_csv=False, create_images=False, arff=False):
        self.__path = os.path.dirname(__file__) + '/audios'
        self.__generate_arff = arff
        self.__labels = ['cat', 'dog']

        if create_images:
            self.__spectrogram_extraction()

        if create_csv:
            self.__create_csv()

    def __spectrogram_extraction(self):
        Logger.log('Executing spectrogram_extraction')

        cmap = plt.get_cmap('inferno')

        plt.figure(figsize=(10, 10))
        animals = self.__labels

        for animal in animals:
            Logger.log(f'Reading data for {animal} animal')
            pathlib.Path(
                f'{self.__path}/spectograms/{animal}').mkdir(parents=True, exist_ok=True)

            for filename in os.listdir(f'{self.__path}/train/{animal}'):
                Logger.log(f'Creating spectogram for {animal}: {filename}')

                audioname = f'{self.__path}/train/{animal}/{filename}'
                y, sr = librosa.load(audioname, mono=True, duration=5)
                plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128,
                             cmap=cmap, sides='default', mode='default', scale='dB')
                plt.axis('off')
                plt.savefig(
                    f'{self.__path}/spectograms/{animal}/{filename[:-3].replace(".", "")}.png')
                plt.clf()

                Logger.log(
                    f'Spectogram created {filename[:-3].replace(".", "")}.png', True)

    def __feature_extraction(self, audioname):
        y, sr = librosa.load(audioname, mono=True, duration=30)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rms = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)

        return chroma_stft, rms, spec_cent, spec_bw, rolloff, zcr, mfcc

    def __create_arff(self, features):
        Logger.log('Generating .ARFF')

        weka_file = 'audio_features.arff'
        weka_header = '''@relation caracteristicas\n
@attribute chromagram real
@attribute rms real
@attribute spectral_centroid real
@attribute spectral_bandwidth real
@attribute rolloff_frequency real
@attribute zero_crossing_rate real
'''
        for i in range(1, 21):
            weka_header += f'@attribute mel_frequency_cepstral_coefficients_{i} real\n'

        weka_header += '''@attribute label {cat, dog}\n
@data\n'''

        weka_body = ''

        for f in features:
            weka_body += ','.join(map(str, f)) + "\n"

        with open(f'{self.__path}/{weka_file}', 'w') as fp:
            fp.write(weka_header)
            fp.write(weka_body)

    def __create_csv(self):
        Logger.log('Executing csv creation')

        header = 'filename chroma_stft rms spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
        for i in range(1, 21):
            header += f' mfcc{i}'
        header += ' label'
        header = header.split()

        file = open(f'{self.__path}/data.csv', 'w', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(header)
        animals = self.__labels

        all_features = []

        for animal in animals:
            Logger.log(f'Reading data for {animal} animal')

            for filename in os.listdir(f'{self.__path}/train/{animal}'):
                Logger.log(f'Creating CSV data for {animal}: {filename}')

                audioname = f'{self.__path}/train/{animal}/{filename}'

                chroma_stft, rms, spec_cent, spec_bw, rolloff, zcr, mfcc = self.__feature_extraction(
                    audioname)

                features = [
                    np.mean(chroma_stft),
                    np.mean(rms),
                    np.mean(spec_cent),
                    np.mean(spec_bw),
                    np.mean(rolloff),
                    np.mean(zcr)
                ]

                to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rms)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'

                for e in mfcc:
                    to_append += f' {np.mean(e)}'
                    features.append((np.mean(e)))

                to_append += f' {animal}'
                features.append(animal)

                file = open(f'{self.__path}/data.csv', 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())

                all_features.append(features)

                Logger.log(f'Data added for CSV file', True)

        if self.__generate_arff:
            self.__create_arff(features=all_features)

    def classify(self, learning_rate, training_time):
        data = pd.read_csv(f'{self.__path}/data.csv')
        data = data.drop(['filename'], axis=1)

        # encoding the labels
        animal_list = data.iloc[:, -1]
        encoder = LabelEncoder()
        y = encoder.fit_transform(animal_list)

        scaler = StandardScaler()
        X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))

        # salva o scaler para ser utilizado no run()
        joblib.dump(scaler, 'std_scaler.bin', compress=True)

        # 20% for tests
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2)

        # length from 20%
        items_for_tests = len(y_test)

        x_val = X_train[:items_for_tests]
        partial_x_train = X_train[items_for_tests:]

        y_val = y_train[:items_for_tests]
        partial_y_train = y_train[items_for_tests:]

        model = models.Sequential()
        model.add(layers.Dense(512, activation='relu',
                               input_shape=(X_train.shape[1],)))
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(2, activation='softmax'))

        adam = optimizers.Adam(
            learning_rate=learning_rate)

        model.compile(optimizer=adam,
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(partial_x_train,
                  partial_y_train,
                  epochs=training_time,
                  batch_size=2056,
                  validation_data=(x_val, y_val),
                  verbose=0
                  )

        model.save_weights(os.path.dirname(__file__) +
                           '/output/model_weights.h5')
        model.save(os.path.dirname(__file__) + '/output/model.h5')

        test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
        Logger.log(f'Accuracy {test_acc} - Loss {test_loss}')

        print(json.dumps({
            'learning-rate': learning_rate,
            'training-time': training_time,
            'accuracy': test_acc,
            'loss': test_loss
        }))

    def run(self, audioname):
        # extract features from selected audio
        chroma_stf, rms, spec_cent, spec_bw, rolloff, zcr, mfcc = self.__feature_extraction(
            audioname)

        new_input = [np.mean(chroma_stf), np.mean(rms), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff),
                     np.mean(zcr)]
        for e in mfcc:
            new_input.append(np.mean(e))

        X = np.array(new_input, dtype=float).reshape(1, -1)

        # carrega o scaler utilizado no __classify()
        scaler = joblib.load('std_scaler.bin')
        X_new = scaler.transform(X)

        model = models.load_model(
            os.path.dirname(__file__) + '/output/model.h5')
        model.load_weights(os.path.dirname(__file__) +
                           '/output/model_weights.h5')

        predictions = model.predict(X_new)
        predict_result = np.argmax(predictions[0])

        features = {
            'Chromagram': str(np.mean(chroma_stf)),
            'RMS': str(np.mean(rms)),
            'Spectral Centroid': str(np.mean(spec_cent)),
            'Spectral Bandwidth': str(np.mean(spec_bw)),
            'Roll-off Frequency': str(np.mean(rolloff)),
            'Zero-crossing rate': str(np.mean(zcr))
        }

        for e in mfcc:
            features.update(
                {'Mel-frequency cepstral coefficients': str(np.mean(e))})

        Logger.log(f'Using passed audio')
        Logger.log(f'Result for {audioname} = {self.__labels[predict_result]}')

        print(json.dumps({
            'audioname': audioname,
            'features': features,
            'result': self.__labels[predict_result],
        }))


if __name__ == "__main__":

    action = sys.argv[1]

    if action == 'training':
        if len(sys.argv) < 4:
            Logger.log(f'Missing parameters! Check again :)')
        else:
            learning_rate = float(sys.argv[2])
            training_time = int(sys.argv[3])

            """
            When arff is True then create_csv should be True
            """
            ClassifyAudio(create_csv=True, arff=True).classify(
                learning_rate=learning_rate, training_time=training_time)
    elif action == 'classify':
        if len(sys.argv) < 3:
            Logger.log(f'Missing the audio path!')
        else:
            file = sys.argv[2]

            ClassifyAudio().run(audioname=file)
