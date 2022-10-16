from email.policy import default
from enum import unique
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField(null=True, blank=True)
    address =models.CharField(max_length=500, null=True, blank=True)
    logo = models.ImageField(upload_to="company/logo", default="logo.jpg")

    def __str__(self):
        return self.name


class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    created_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.branch_name   



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



class Skill(models.Model):
    LEVEL = (
        ("Starter", "Starter"),
        ("Basic", "Basic"),
        ("Cofortable", "Cofortable"),
        ("Skillfull", "Skillfull"),
        ("Master", "Master"),
    )
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    level_of_mastery = models.CharField(max_length=20, choices=LEVEL, null=True, blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    sample_photo = models.ImageField(upload_to="projects/", default="project.jpg")
    likes = models.ManyToManyField(Advocate, null=True, blank=True, related_name="likes")
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

# ? which technologies and tools have employed to create the project?
class Tech(models.Model):
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    tech = models.CharField(max_length=200)

    def __str__(self):
        return self.tech

