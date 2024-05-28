from django.urls import path
from .views import UserRegistrationView, LogoutView, UserLoginView
from .views import SignMessageView, VerifyMessageView, EncryptMessageView, DecryptMessageView, HashMessageView

app_name = 'accounts'

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="user_logout"),
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("sign_message/", SignMessageView.as_view(), name="sign_message"),
    path("verify_message/", VerifyMessageView.as_view(), name="verify_message"),
    path("encrypt_message/", EncryptMessageView.as_view(), name="encrypt_message"),
    path("decrypt_message/", DecryptMessageView.as_view(), name="decrypt_message"),
    path("hash_message/", HashMessageView.as_view(), name="hash_message"),
]
