import os
import pickle
import image_slicer
from requests.auth import HTTPBasicAuth
import requests, json

def test():
    test_image = ''
    img = image.load_img('assets/test/'+test_image, target_size=(256, 256), color_mode='grayscale')
    img = image.img_to_array(img)
    img = img / 255
    test_image.append(img)
    test = np.array(test_image)

    with open(model_location + 'plant_mode.pkl', 'wb') as file_loc:
        pickle.dump(model, file_loc)


    prediction = model.predict(test)
    prediction_cl = model.predict_classes(test)

    print(prediction)
    print('............')
    print(prediction_cl)


# test()




