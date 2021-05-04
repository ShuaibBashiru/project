from django.urls import path
from . import views, auth, accounts, mailer


urlpatterns = [
    path('', views.index, name="home"),
    path('sign_in/', auth.authenticate, name="sign_to_portal"),
    path('new_account/', accounts.create_acccount, name="create_acccount"),
    path('secure_otp/', mailer.mailpasscode, name="mail_passcode"),
    path('tokenize/', auth.token_nizer, name="tokenize_csrf"),
    path('auth_check/', auth.auth_check_session, name="check_session"),
    path('logout/', auth.logout_session, name="auth_logout_session"),
]
