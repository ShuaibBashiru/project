from django.urls import path
from . import views, widget

urlpatterns = [
    # path('', views.index, name="home"),
    path('widget/', widget.add_widget, name="add_widget"),
    path('update_widget/', widget.update_widget, name="update_widget"),
    path('update_widget_status/', widget.update_widget_status, name="update_widget_status"),
    path('delete_widget/', widget.delete_widget, name="delete_widget"),
]