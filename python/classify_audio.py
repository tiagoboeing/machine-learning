# feature extractoring and preprocessing data
import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import pathlib
import csv

# Preprocessing
from sklearn import preprocessing, model_selection, metrics

# Classification
from sklearn.neural_network import MLPClassifier

import warnings

warnings.filterwarnings('ignore')


class ClassifyAudio():
    def __init__(self, learning_rate, training_time):
        self.__path = './audios'
        self.__learning_rate = learning_rate
        self.__training_time = training_time
        self.__labels = ['cat', 'dog']

    def __spectrogram_extraction(self):
        cmap = plt.get_cmap('inferno')

        plt.figure(figsize=(10, 10))
        animals = 'cat dog'.split()
        for a in animals:
            pathlib.Path(
                f'{self.__path}/spectograms/{a}').mkdir(parents=True, exist_ok=True)
            for filename in os.listdir(f'{self.__path}/{a}'):
                audioname = f'{self.__path}/{a}/{filename}'
                y, sr = librosa.load(audioname, mono=True, duration=5)
                plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128,
                             cmap=cmap, sides='default', mode='default', scale='dB')
                plt.axis('off')
                plt.savefig(
                    f'{self.__path}/spectograms/{a}/{filename[:-3].replace(".", "")}.png')
                plt.clf()

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
        header = 'filename chroma_stft rms spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
        for i in range(1, 21):
            header += f' mfcc{i}'
        header += ' label'
        header = header.split()

        file = open('data.csv', 'w', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(header)
        animals = 'cat dog'.split()
        for a in animals:
            for filename in os.listdir(f'{self.__path}/{a}'):
                audioname = f'{self.__path}/{a}/{filename}'

                chroma_stft, rms, spec_cent, spec_bw, rolloff, zcr, mfcc = self.__feature_extraction(
                    audioname)

                to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rms)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
                for e in mfcc:
                    to_append += f' {np.mean(e)}'
                to_append += f' {a}'
                file = open('data.csv', 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(to_append.split())

    def __classify(self):
        data = pd.read_csv('data.csv')
        data = data.drop(['filename'], axis=1)

        animal_list = data.iloc[:, -1]
        encoder = preprocessing.LabelEncoder()
        y = encoder.fit_transform(animal_list)

        X = np.array(data.iloc[:, :-1], dtype=float)

        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            X, y, test_size=0.2)

        scaler = preprocessing.StandardScaler()
        scaler.fit(X_train)

        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

        mlp = MLPClassifier(
            solver='adam', learning_rate_init=self.__learning_rate, max_iter=self.__training_time)

        mlp.fit(X_train, y_train)
        print("Training set score: %f" % mlp.score(X_test, y_test))
        # print("Training set loss: %f" % mlp.loss_)

        return mlp

    def run(self, audioname):
        new_input = []

        model = self.__classify()

        chroma_stft, rms, spec_cent, spec_bw, rolloff, zcr, mfcc = self.__feature_extraction(
            audioname=audioname)

        new_input.append(np.mean(chroma_stft))
        new_input.append(np.mean(rms))
        new_input.append(np.mean(spec_cent))
        new_input.append(np.mean(spec_bw))
        new_input.append(np.mean(rolloff))
        new_input.append(np.mean(zcr))

        for e in mfcc:
            new_input.append(np.mean(e))

        X = np.array(new_input, dtype=float).reshape(1, -1)

        predictions = model.predict(X)[0]
        print(self.__labels[predictions])


ClassifyAudio(learning_rate=0.3, training_time=200).run(
    audioname="./audios/dog/dog_barking_70.wav")
