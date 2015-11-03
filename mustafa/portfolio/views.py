from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import BasicInformation
from .models import Project
from .models import Experience
from .models import Language


def about(request):
    basic_information = BasicInformation.objects.latest('pk')
    template = loader.get_template('portfolio/index.html')
    context = RequestContext(request, {
        'basic_information': basic_information,
    })
    return HttpResponse(template.render(context))


def projects(request):
    basic_information = BasicInformation.objects.latest('pk')
    projects_list = Project.objects.all()
    languages = Language.objects.all()
    template = loader.get_template('portfolio/projects.html')
    context = RequestContext(request, {
        'basic_information': basic_information,
        'projects': projects_list,
        'languages': languages,
    })
    return HttpResponse(template.render(context))


def experience(request):
    basic_information = BasicInformation.objects.latest('pk')
    experience_list = Experience.objects.all()
    languages = Language.objects.all()
    template = loader.get_template('portfolio/experience.html')
    context = RequestContext(request, {
        'basic_information': basic_information,
        'experience': experience_list,
        'languages': languages,
    })
    return HttpResponse(template.render(context))
