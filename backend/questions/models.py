from django.db import models
from interview.models import InterviewExperience
from accounts.models import CustomUser
from company.models import Company

class QuestionModel(models.Model):
    interview = models.ForeignKey(InterviewExperience,related_name="interview_questions",on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,related_name="user",on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete= models.CASCADE)
    question = models.TextField()
    answer = models.TextField(blank=True)
    category = models.CharField(max_length=40,default="Unknown")


    def __str__(self) :
        return self.question