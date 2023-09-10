from django.shortcuts import render
from rest_framework import generics
from .models import Company
from .serializers import CompanySerilizer

class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerilizer
    http_method_names = ('get',)


