from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, blank= False, unique= True)
    description = models.TextField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    headquarters = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    #logo = models.ImageField(upload_to='company_logos/', blank=True)

    def __str__(self) : 
        return self.name

