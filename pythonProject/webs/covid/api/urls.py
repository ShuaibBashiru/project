from django.urls import path
from . import views, testfile, upload, gets, traindata


urlpatterns = [
    path('', views.index, name="home"),
    path('test/', testfile.testing, name="home"),
    path('upload/', upload.upload, name="uploader"),
    path('list_dataset/', gets.get_dataset, name="get_dataset"),
    path('train_data/', traindata.train_data, name="train_data"),
    path('modelanalysis/', traindata.model_analysis, name="model_analysis"),
]
