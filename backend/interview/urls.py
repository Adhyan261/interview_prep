from django.urls import path,include
from .views import InterviewView,InterviewUpdateView,UserInterviewsView,CompanyInterviewsView



urlpatterns = [
    path('interview/', InterviewView.as_view(),),
    path('interview/<int:pk>/', InterviewUpdateView.as_view(),),
    path('interview/user/<int:user_id>/', UserInterviewsView.as_view(),),
    path('interview/company/', CompanyInterviewsView.as_view(),),
]