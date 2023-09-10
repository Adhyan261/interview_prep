from django.urls import path,include
from .views import CompanyView




urlpatterns = [
    path('company/', CompanyView.as_view(),),
]