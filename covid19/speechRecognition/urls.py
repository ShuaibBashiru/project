from django.urls import path
from . import views, sourcecode, inserts, gets

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/<int:app_oath>/', sourcecode.upload, name='upload'),
    path('csv_reader/<int:app_oath>/', sourcecode.csv_reader, name='csv_reader'),
    path('send_message/<int:app_oath>/', sourcecode.send_message, name='send_message'),
    path('analyze/<int:app_oath>/', inserts.analyze, name='analyze'),
    path('create_voice/<int:app_oath>/', inserts.create_voice, name='create_voice'),
    path('voice_captured/<int:app_oath>/', gets.voice_captured, name='voice_captured'),
]
