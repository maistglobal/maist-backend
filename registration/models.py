from django.db import models

class TechProvider(models.Model):
    industry_type = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, unique=True)
    company_registered_number = models.CharField(max_length=50, unique=True)
    company_address = models.TextField()
    primary_email = models.EmailField(unique=True)
    linkedin_link = models.URLField()

class TechSeeker(models.Model):
    company_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    linkedin_link = models.URLField()
    contact_number = models.CharField(max_length=15)