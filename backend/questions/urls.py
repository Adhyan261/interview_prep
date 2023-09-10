from django.urls import path,include
from .views import QuestionView,EditQuestionView,QuestionSearchView, CompanyQuestionSearchView




urlpatterns = [
    path('questions/', QuestionView.as_view(),),
    path('questions/<int:pk>',EditQuestionView.as_view(),),
    path('questions/search/',QuestionSearchView.as_view(),),
    path('questions/company/',CompanyQuestionSearchView.as_view(),)
]