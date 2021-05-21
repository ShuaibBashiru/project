from django.urls import path
from . import widget, admin_menu, password, admin_menu_approval


urlpatterns = [
    path('adminmenu/menus/', admin_menu.admin_menus, name="admin_menus"),
    path('adminmenu/list/', admin_menu.list, name="adminmenulist"),
    path('adminmenu/filter/', admin_menu.list_filter, name="adminmenufilter"),
    path('adminmenu/search/', admin_menu.list_search, name="adminmenusearch"),
    path('adminmenu/download/', admin_menu.download, name="adminmenudownload"),
    path('adminmenu/validate_id/', widget.preview, name="adminmenu_preview"),

    path('adminmenuapproval/list/', admin_menu_approval.list, name="adminmenuapprovallist"),
    path('adminmenuapproval/filter/', admin_menu_approval.list_filter, name="adminmenuapprovalfilter"),
    path('adminmenuapproval/search/', admin_menu_approval.list_search, name="adminmenuapprovalsearch"),
    path('adminmenuapproval/download/', admin_menu_approval.download, name="adminmenuapprovaldownload"),

    path('widget/list/', widget.list, name="widget_list"),
    path('widget/filter/', widget.list_filter, name="widget_list_filter"),
    path('widget/search/', widget.list_search, name="widget_list_search"),
    path('widget/download/', widget.download, name="download_widget"),
    path('widget/validate_id/', widget.preview, name="widget_preview"),

    path('validate_password_id/', password.validate_password_id, name="validate_password_id"),

    # path('user_record/', gets.user_record, name="user_record"),
    # path('admin_record/', gets.admin_record, name="admin_record"),
]
