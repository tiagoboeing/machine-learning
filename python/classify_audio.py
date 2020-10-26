import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import pathlib
import csv
from logger import Logger

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Keras
import keras
from keras import models
from keras import layers

import warnings

warnings.filterwarnings('ignore')


class ClassifyAudio():
    def __init__(self, learning_rate, training_time, create_csv=True, create_images=False):
        self.__path = './audios'
        self.__learning_rate = learning_rate
        self.__training_time = training_time
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

                Logger.log(f'Spectogram created {filename[:-3].replace(".", "")}.png', True)

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

        for animal in animals:
            Logger.log(f'Reading data for {animal} animal')

            for filename in os.listdir(f'{self.__path}/train/{animal}'):
                Logger.log(f'Creating CSV data for {animal}: {filename}')

                audioname = f'{self.__path}/train/{animal}/{filename}'

                chroma_stft, rms, spec_cent, spec_bw, rolloff, zcr, mfcc = self.__feature_extraction(
                    audioname)

                to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rms)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'

                for e in mfcc:
                    to_append += f' {np.mean(e)}'
                to_append += f' {animal}'

                file = open(f'{self.__path}/data.csv', 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())

                Logger.log(f'Data added for CSV file', True)

    def __classify(self):
        data = pd.read_csv(f'{self.__path}/data.csv')
        data = data.drop(['filename'], axis=1)

        # encoding the labels
        animal_list = data.iloc[:, -1]
        encoder = LabelEncoder()
        y = encoder.fit_transform(animal_list)

        scaler = StandardScaler()
        X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype=float))

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
        model.add(layers.Dense(512, activation='relu', input_shape=(X_train.shape[1],)))
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(partial_x_train,
                  partial_y_train,
                  epochs=30,
                  batch_size=512,
                  validation_data=(x_val, y_val)
                  )

        test_loss, test_acc = model.evaluate(X_test, y_test)
        Logger.log(f'Accuracy {test_acc} - Loss {test_loss}')

        predictions = model.predict(X_test)

        return model, test_loss, test_acc, predictions

    def run(self, audioname):
        model, test_loss, test_acc, predictions = self.__classify()

        Logger.log(f'Loss: {test_loss}')
        Logger.log(f'Accuracy: {test_acc}', True)

        # with test data
        predictions_sum = np.sum(predictions[0])
        result = np.argmax(predictions[0])

        Logger.log(f'Using test data')
        Logger.log(f'Predictions SUM: {predictions_sum}')
        Logger.log(f'Result: {result} = {self.__labels[result]}', True)

        # extract features from selected audio
        chroma_stf, rms, spec_cent, spec_bw, rolloff, zcr, mfcc = self.__feature_extraction(audioname)

        new_input = [np.mean(chroma_stf), np.mean(rms), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff),
                     np.mean(zcr)]
        for e in mfcc:
            new_input.append(np.mean(e))

        X = np.array(new_input, dtype=float).reshape(1, -1)

        predict_result = int(model.predict(X)[0][0])
        Logger.log(f'Using passed audio')
        Logger.log(f'Result for {audioname} = {self.__labels[predict_result]}')


# weka = Weka('./audios/dog')
# print(weka.list_directory_files())
# weka.create_audio_file('caracteristicas-audio')

ClassifyAudio(learning_rate=0.3, training_time=1000, create_images=False, create_csv=False).run(
    audioname="./audios/test/dog/dog_barking_24.wav")
