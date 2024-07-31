
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('vote', vote, name="vote"),  # URL pattern for /vote/<id>/
    path('result/', result, name="result"),
    path('register/', register, name='register'),
    path('login/', log_in, name='log_in'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', log_out, name='log_out'),
    # Password reset setup
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name="password_reset_complete"),
]

