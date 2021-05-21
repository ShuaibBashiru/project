from django.urls import path
from . import views, widget, admin_account, password, admin_menu, admin_menu_approval

urlpatterns = [
    # path('', views.index, name="home"),
    path('widget/new/', widget.addNew, name="newwidget"),
    path('widget/update', widget.update, name="update_widget"),
    path('widget/update_status/', widget.update_status, name="update_widget_status"),
    path('widget/delete/', widget.delete, name="delete_widget"),

    path('newaccount/', admin_account.addNew, name="newaccount"),
    path('validate_email_id/', password.validate_email_id, name="validate_email_id"),
    path('update_password/', password.update_password, name="update_password"),

    path('adminmenu/new/', admin_menu.addNew, name="newmenu"),
    path('adminmenu/update_status/', admin_menu.update_status, name="adminmenu_status"),

    path('adminmenuapproval/update_status/', admin_menu_approval.update_status, name="adminmenuapproval_status"),
    path('adminmenuapproval/access/', admin_menu_approval.access, name="adminmenuaccess"),

]
