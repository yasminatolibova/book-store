from .views import RegisterAPI, LoginView, LogoutView, ResetPasswordAPI
from django.urls import path


urlpatterns=[
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('reset_password/', ResetPasswordAPI.as_view()),
]