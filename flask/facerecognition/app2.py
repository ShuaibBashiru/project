import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("FACE CAPTURE PANEL")
img_counter = 0
while True:
    ret, frame = cam.read()
    cv2.imshow("FACE CAPTURE PANEL", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    if k%256 == 27:
    # ESC pressed
        cam.release()
        cv2.destroyAllWindows()
        # redirect("/dashboard", code=302)
        break
    elif k%256 == 32:
    # SPACE pressed
        newuserid='newface'
        img_name = "{}.png".format(newuserid)
        cv2.imwrite('static/document/unknown/'+img_name, frame)
        print("{} written!".format(img_name))
        cam.release()
        cv2.destroyAllWindows()
        message={
            "msg":"created",
            "filename":img_name
        }
        print(message)
cam.release()
cv2.destroyAllWindows()



# import face_recognition
# import os
# positive=0
# negative=0
# images = os.listdir('static/document/known/')
# # load your image
# image_to_be_matched = face_recognition.load_image_file('static/document/unknown/newface.png')
# # encoded the loaded image into a feature vector
# image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
# # iterate over each image
# for image in images:
#     # load the image
#     current_image = face_recognition.load_image_file("static/document/known/"+image)
#     # encode the loaded image into a feature vector
#     current_image_encoded = face_recognition.face_encodings(current_image)[0]
#     # match your image with the image and check if it matches
#     result = face_recognition.compare_faces(
#         [image_to_be_matched_encoded], current_image_encoded, tolerance=0.30)
#     # check if it was a match
#     if result[0] == True:
#         positive+=1
#     else:
#         negative+=1
# message={
# 'positive':positive,
# 'negative':negative
# }
# print(message)
