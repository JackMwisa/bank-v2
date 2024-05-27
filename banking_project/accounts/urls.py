from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('encrypt/', views.encrypt_data, name='encrypt'),
    path('decrypt/', views.decrypt_data, name='decrypt'),
    path('sign/', views.sign_data, name='sign'),
    path('verify/', views.verify_signature, name='verify'),
    # Add other URL patterns
]
