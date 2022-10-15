from email.policy import default
from enum import unique
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField(null=True, blank=True)
    address =models.CharField(max_length=500, null=True, blank=True)
    logo = models.ImageField(upload_to="company/logos", default="logo.jpg")

    def __str__(self):
        return self.name



class Advocate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    short_bio = models.CharField(max_length=500)
    long_bio = models.TextField(null=True, blank=True)
    years_of_exp = models.SmallIntegerField(default=1)
    profile_pic = models.ImageField(upload_to="advocate/profile", default="profile.jpg")

    def __str__(self):
        return self.name

class SocialAccount(models.Model):
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    account_url = models.URLField(max_length=200, unique=True)
    member_since = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name