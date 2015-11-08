from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext_lazy as _


class BasicInformation(SingletonModel):
    name = models.CharField(max_length=25, default="John Smith")
    short_bio = models.CharField(max_length=100,
                                 blank=True,
                                 verbose_name=_("short bio"),
                                 default="My short bio")
    long_bio = models.TextField(blank=True,
                                verbose_name=_("long bio"),
                                default="My long bio")
    email = models.EmailField(default="email@example.com")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    image = models.ImageField(blank=True)

    def __repr__(self):
        return '<BasicInformation: %s>' % self.name

    def __str__(self):
        return self.name.title()


class Education(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=10, blank=True, default=None)
    abbreviation = models.CharField(max_length=10, blank=True, default=None)
    major = models.CharField(max_length=15, blank=True, default=None)
    gpa = models.CharField(max_length=10, blank=True, default=None)

    def __repr__(self):
        return '<Education: %s>' % self.name

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200, blank=True)
    conference = models.CharField(max_length=200, blank=True)
    abstract = models.TextField(blank=True)
    year = models.CharField(max_length=4, blank=True)
    link = models.URLField(blank=True)

    def __repr__(self):
        return '<Publication: %s>' % self.name

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default=None,
                                   blank=True,
                                   verbose_name=_("description"))
    start_date = models.DateField(null=True, blank=True,
                                  verbose_name=_("start date"))
    end_date = models.DateField(null=True, blank=True,
                                verbose_name=_("end date"))
    link = models.URLField(blank=True)

    def __repr__(self):
        return '<Project: %s>' % self.name

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=150)
    start_date = models.DateField(null=True, blank=True,
                                  verbose_name=_("start date"))
    end_date = models.DateField(null=True, blank=True,
                                verbose_name=_("end date"))
    description = models.TextField(default=None,
                                   verbose_name=_("description"))
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True)


    def __repr__(self):
        return '<Experience: %s>' % self.company

    def __str__(self):
        return '%s at %s' % (self.role.capitalize(), self.company)


class Language(models.Model):
    name = models.CharField(max_length=20)
    experience = models.ManyToManyField(Experience, null=True, blank=True, default=None)
    projects = models.ManyToManyField(Project, null=True, blank=True, default=None)

    def __repr__(self):
        return '<Language: %s>' % self.name

    def __str__(self):
        return self.name
