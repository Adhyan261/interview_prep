from django.db import models
from company.models import Company
#from django.contrib.auth.models import User  
from accounts.models import CustomUser


class InterviewExperience(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    interview_date = models.DateField()
    interview_round = models.PositiveIntegerField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.id) + ' '+str(self.company)}"



