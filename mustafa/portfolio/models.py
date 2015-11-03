from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class BasicInformation(models.Model):
    site = models.OneToOneField(Site)
    name = models.CharField(max_length=20)
    short_bio = models.CharField(max_length=200,
                                 verbose_name=_("short bio"))
    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedIn = models.URLField(blank=True)
    image = models.ImageField()

    def __repr__(self):
        return '<BasicInformation: %s>' % self.name

    def __str__(self):
        return self.name.title()


class Project(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200,
                                   verbose_name=_("description"))
    link = models.URLField()
    picture = models.ImageField()

    def __repr__(self):
        return '<Project: %s>' % self.name

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    start_date = models.TimeField(verbose_name=_("start date"))
    end_date = models.TimeField(verbose_name=_("end date"))
    description = models.CharField(max_length=200,
                                   verbose_name=_("description"))
    URL = models.URLField(blank=True)

    def __repr__(self):
        return '<Experience: %s>' % self.company

    def __str__(self):
        return '%s at %s' % self.name.capitalize(), self.company


class Language(models.Model):
    name = models.CharField(max_length=10)
    experience = models.ForeignKey(Experience, null=True, blank=True, default=None)
    projects = models.ForeignKey(Project, null=True, blank=True, default=None)

    def __repr__(self):
        return '<Language: %s>' % self.name

    def __str__(self):
        return self.name
