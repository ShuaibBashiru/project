from django.urls import path
from . import api_widget, menus


urlpatterns = [
    path('admin_menus/', menus.admin_menus, name="admin_menus"),
    path('widget/', api_widget.widget_list, name="widget_list"),
    path('widgetfilter/', api_widget.widget_list_filter, name="widget_list_filter"),
    path('widgetsearch/', api_widget.widget_list_search, name="widget_list_search"),
    path('download_widget/', api_widget.download_widget, name="download_widget"),
    path('validate_id/', api_widget.widget_preview, name="widget_preview"),
    # path('getuserdata_invoice/', gets.get_user_data_invoice, name="get_user_data_invoice"),
    # path('getinvoice/', gets.get_invoice, name="get_invoice"),
    # path('invoices/', gets.invoices, name="invoices"),
    # path('getinvoicedata/', gets.get_invoice_data, name="get_invoice_data"),
    # path('flaggedlist/', gets.flagged_list, name="flagged_lists"),
    # path('user_record/', gets.user_record, name="user_record"),
    # path('admin_record/', gets.admin_record, name="admin_record"),
]
