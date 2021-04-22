import os
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm
import image_slicer
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from google.colab import auth
# from oauth2client.client import GoogleCredentials
#
# auth.authenticate_user()
# gauth = GoogleAuth()
# gauth.credentials = GoogleCredentials.get_application_default()
# drive = GoogleDrive(gauth)

# download = drive.CreateFile({'id': '1BZOv422XJvxFUnGh-0xVeSvgFgqVY45q'})
# download.GetContentFile('train_LbELtWX.zip')

# image_slicer.slice('assets/train/5.jpeg', 20)


def test():
    train = pd.read_csv('assets/train.csv')
    train_image = []
    for i in tqdm(range(train.shape[0])):
        img = image.load_img('assets/train/' + train['id'][i].astype('str') + '.jpeg', target_size=(28, 28, 1), grayscale=True)
        img = image.img_to_array(img)
        img = img / 255
        train_image.append(img)
    X = np.array(train_image)
    y = train['label'].values
    y = to_categorical(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['binary_accuracy', 'categorical_accuracy'])
    model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
    # print(model.summary())

    test = pd.read_csv('assets/test.csv')
    test_image = []
    for i in tqdm(range(test.shape[0])):
        img = image.load_img('assets/test/' + test['id'][i].astype('str') + '.jpeg', target_size=(28, 28, 1),
                             grayscale=True)
        img = image.img_to_array(img)
        img = img / 255
        test_image.append(img)
    test = np.array(test_image)
    prediction = model.predict(test)
    prediction_cl = model.predict_classes(test)
    print(prediction)
    print('............')
    print(prediction_cl)


# test()
