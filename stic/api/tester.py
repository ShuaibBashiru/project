import os
import cv2
import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
from PIL import Image
from keras.applications.imagenet_utils import decode_predictions
from keras.models import model_from_json
from keras.models import load_model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm
from requests.auth import HTTPBasicAuth
import requests, json
import joblib
from collections import Counter
from PIL import Image


def test():
    train_image = []
    category = []
    rootdir = '/content/drive/MyDrive/dataset_plant/'
    model_location = '/content/drive/MyDrive/plant_model/model_output.h5'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # print(os.path.join(subdir, file))
            img = image.load_img(os.path.join(subdir, file), color_mode='rgb',
                                 target_size=(256, 256), interpolation="nearest")
            # print(img)
            img = image.img_to_array(img)
            img = img / 255
            train_image.append(img)

            getdir = subdir.split('/')
            if str(getdir[5]) == 'Tomato___Bacterial_spot':
                classname = 1
            elif str(getdir[5]) == 'Tomato___Early_blight':
                classname = 2
            elif str(getdir[5]) == 'Tomato___Late_blight':
                classname = 3
            elif str(getdir[5]) == 'Tomato___Leaf_Mold':
                classname = 4
            elif str(getdir[5]) == 'Tomato___Septoria_leaf_spot':
                classname = 5
            elif str(getdir[5]) == 'Tomato___Spider_mitesTwo-spotted_spider_mite':
                classname = 6
            elif str(getdir[5]) == 'Tomato___Target_Spot':
                classname = 7
            elif str(getdir[5]) == 'Tomato___Tomato_Yellow_Leaf_Curl_Virus':
                classname = 8
            elif str(getdir[5]) == 'Tomato___Tomato_mosaic_virus':
                classname = 9
            elif str(getdir[5]) == 'Tomato___healthy':
                classname = 0
            else:
                classname = -1

            category.append(classname)

    num_class = (len(set(category)))

    X = np.array(train_image)
    y = category
    y = to_categorical(y, num_classes=num_class)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

    model = Sequential()

    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', strides=(1, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten(input_shape=(None, 256, 256, 3)))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(num_class, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='Adam',
                  metrics=['accuracy', 'categorical_accuracy'])

    model.fit(X_train, y_train,
              batch_size=100,
              epochs=10,
              verbose=1,
              validation_data=(X_test, y_test))

    model.save(model_location)




def res():
  model_location = '/content/drive/MyDrive/plant_model/model_output.h5'
  rootdir = '/content/drive/MyDrive/dataset_test/'

  model = load_model(model_location)
  test_images = []
  results = []
  for subdir, dirs, files in os.walk(rootdir):
    for filename in files:
      img = Image.open(rootdir+filename)
      h = 256
      w = 256
      img = img.resize((w, h), Image.ANTIALIAS)
      img = image.img_to_array(img)
      img = tf.image.rgb_to_grayscale(x)
      img = np.expand_dims(x, axis=0)
      img = x/255
      test_images.append(x)
      output = model.predict(x)
      indexes = tf.argmax(output, axis=1)
      individual = indexes.numpy()
      results.append(individual[0])

  print(results)
