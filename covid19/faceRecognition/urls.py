from django.urls import path
from . import views, upload, inserts, gets

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/<int:app_oath>/', upload.upload, name='upload'),
    path('uploadcourses/<int:app_oath>/', upload.uploadcourses, name='uploadcourses'),
    path('send_message/<int:app_oath>/', upload.send_message, name='send_message'),
    path('analyze/<int:app_oath>/', inserts.analyze, name='analyze'),
    path('create_voice/<int:app_oath>/', inserts.create_voice, name='create_voice'),
    path('bio_data/<int:app_oath>/', gets.bio_data, name='bio_data'),
    path('courses/<int:app_oath>/', gets.courses, name='courses'),
    path('listdataface/<int:app_oath>/', gets.listdataface, name='listdataface'),
    path('capturephoto/<int:app_oath>/', gets.capturephoto, name='capturephoto'),
    path('match_image/<int:app_oath>/', gets.match_image, name='match_image'),
    path('match_image_external/<int:app_oath>/', gets.match_image_external, name='match_image_external'),
]
