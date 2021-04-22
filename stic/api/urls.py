from django.urls import path
from . import gets, tester


urlpatterns = [
    path('get_drug_list/', gets.get_drug_list, name="get_drug_list"),
    path('get_user_data/', gets.get_user_data, name="get_user_data"),
    path('getuserdata_invoice/', gets.get_user_data_invoice, name="get_user_data_invoice"),
    path('getinvoice/', gets.get_invoice, name="get_invoice"),
    path('invoices/', gets.invoices, name="invoices"),
    path('getinvoicedata/', gets.get_invoice_data, name="get_invoice_data"),
    path('flaggedlist/', gets.flagged_list, name="flagged_lists"),
    path('user_record/', gets.user_record, name="user_record"),
    path('admin_record/', gets.admin_record, name="admin_record"),
    path('tester/', tester.test, name="tester"),
]
