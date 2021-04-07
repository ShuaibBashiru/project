from django.urls import path
from . import views, authentication, gets, inserts

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', authentication.signin, name='signIn'),
    path('compare_voice/', gets.compare_voice, name='compare_voice'),
    path('enroll_voice/', inserts.enroll_voice, name='enroll_voice'),
]
