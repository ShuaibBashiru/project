from django.urls import path
from . import views, widget, adminAccount, password

urlpatterns = [
    # path('', views.index, name="home"),
    path('widget/', widget.add_widget, name="add_widget"),
    path('update_widget/', widget.update_widget, name="update_widget"),
    path('update_widget_status/', widget.update_widget_status, name="update_widget_status"),
    path('delete_widget/', widget.delete_widget, name="delete_widget"),

    path('newaccount/', adminAccount.add_account, name="newaccount"),
    path('validate_email_id/', password.validate_email_id, name="validate_email_id"),
    path('update_password/', password.update_password, name="update_password"),

]