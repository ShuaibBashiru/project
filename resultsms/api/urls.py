from django.urls import path
from . import upload, gets, tester

urlpatterns = [
    path('upload_sms_list/', upload.sms_list, name="sms_list"),
    path('get_sms_list/', gets.get_sms_list, name="get_sms_list"),
    path('get_sms_list_select/', gets.get_sms_list_select, name="get_sms_list_select"),
    path('send_sms/', gets.send_sms, name="send_sms"),
    path('test/', tester.test, name="test"),
]
