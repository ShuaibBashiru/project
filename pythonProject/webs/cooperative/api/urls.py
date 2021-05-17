from django.urls import path
from . import widget, menus, password


urlpatterns = [
    path('admin_menus/', menus.admin_menus, name="admin_menus"),
    path('widget/', widget.widget_list, name="widget_list"),
    path('widgetfilter/', widget.widget_list_filter, name="widget_list_filter"),
    path('widgetsearch/', widget.widget_list_search, name="widget_list_search"),
    path('download_widget/', widget.download_widget, name="download_widget"),
    path('validate_id/', widget.widget_preview, name="widget_preview"),
    path('validate_password_id/', password.validate_password_id, name="validate_password_id"),

    # path('user_record/', gets.user_record, name="user_record"),
    # path('admin_record/', gets.admin_record, name="admin_record"),
]
