from django.shortcuts import render
from .models import QuestionModel
from .serializers import QuestionSerializer
from rest_framework import generics, filters
from accounts.permissions import IsOwnerOrReadOnly

class QuestionView(generics.ListAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get']

class EditQuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = QuestionModel.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ('get','put','delete',)

class QuestionSearchView(generics.ListAPIView):
    search_fields = ['question']
    filter_backends = (filters.SearchFilter,)
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class CompanyQuestionSearchView(generics.ListAPIView):
    search_fields = ['company__name']
    filter_backends = (filters.SearchFilter,)
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

    


