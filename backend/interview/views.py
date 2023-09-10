from django.shortcuts import render
from rest_framework import generics, filters
from .models import InterviewExperience
from .serializers import InterviewReadSerilizer, InterviewWriteSerilizer
from accounts.permissions import CustomPermission, IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from company.models import Company
#from accounts .models import CustomUser

class InterviewView(generics.ListCreateAPIView):

    queryset = InterviewExperience.objects.all()
    permission_classes = [CustomPermission]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return InterviewWriteSerilizer
        return InterviewReadSerilizer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    

class InterviewUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InterviewExperience.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return InterviewWriteSerilizer
        return InterviewReadSerilizer
    permission_classes =[IsOwnerOrReadOnly]


class UserInterviewsView(generics.ListAPIView):
    serializer_class = InterviewReadSerilizer

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Assuming you pass user_id as a URL parameter
        return InterviewExperience.objects.filter(user=user_id)


class CompanyInterviewsView(generics.ListAPIView):
    search_fields = ['company__name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = InterviewReadSerilizer
    queryset = InterviewExperience.objects.all()
    #def get_queryset(self):
     #   company_name = self.kwargs['company']
      #  company_id = get_object_or_404(Company,name=company_name)
       # return InterviewExperience.objects.filter(company = company_id)


