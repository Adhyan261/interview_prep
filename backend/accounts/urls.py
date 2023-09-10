from django.urls import path
from .views import UserLoginView,UserLogoutView,RegisterUserView,ChangePasswordView,UserProfileView

urlpatterns = [
    path('register/',RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]