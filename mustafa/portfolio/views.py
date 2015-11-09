from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import BasicInformation
from .models import Project
from .models import Experience
from .models import Publication
from .models import Education

from portfolio import utils


def about(request):
    template = loader.get_template('portfolio/index.html')
    basic_information = BasicInformation.objects.get()
    context_dict = {"portfolio_basicinformation": basic_information}
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))


def projects(request):
    basic_information = BasicInformation.objects.latest('pk')
    projects_list = Project.objects.all()
    used_languages = {}
    for project in projects_list:
        used_languages.update(project.get_languages())
    template = loader.get_template('portfolio/projects.html')
    context_dict = {'portfolio_basicinformation': basic_information,
                    'portfolio_project': projects_list,
                    'used_languages': used_languages,
                    }
    print context_dict
    context = RequestContext(request,
                             utils.used_models(context_dict,
                                               ignore_models=["portfolio_language"]))
    return HttpResponse(template.render(context))


def experience(request):
    basic_information = BasicInformation.objects.latest('pk')
    experience_list = Experience.objects.all()
    used_languages = {}
    for experience in experience_list:
        used_languages.update(experience.get_languages())
    template = loader.get_template('portfolio/experience.html')
    context_dict = {'portfolio_basicinformation': basic_information,
                    'portfolio_experience': experience_list,
                    'used_languages': used_languages,
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))


def publications(request):
    basic_information = BasicInformation.objects.latest('pk')
    publication_list = Publication.objects.all()
    template = loader.get_template('portfolio/publications.html')
    context_dict = {'portfolio_basicinformation': basic_information,
                    'portfolio_publication': publication_list,
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))


def education(request):
    basic_information = BasicInformation.objects.latest('pk')
    education_list = Education.objects.all()
    template = loader.get_template('portfolio/education.html')
    context_dict = {'portfolio_basicinformation': basic_information,
                    'portfolio_education': education_list,
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))
