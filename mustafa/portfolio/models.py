from django.db import models
from django.contrib.sites.models import Site


class BasicInformation(models.Model):
    site = models.OneToOneField(Site)
    name = models.CharField(max_length=20)
    short_bio = models.CharField(max_length=200)
    email = models.EmailField()
    github = models.URLField()
    linkedIn = models.URLField()
    image = models.ImageField()


class Projects(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    link = models.URLField()
    picture = models.ImageField()


class Experience(models.Model):
    company = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    start_date = models.TimeField()
    end_date = models.TimeField()
    description = models.CharField(max_length=200)
    URL = models.URLField()


class Languages(models.Model):
    name = models.CharField(max_length=10)
    experience = models.ForeignKey(Experience)
    projects = models.ForeignKey(Projects)
