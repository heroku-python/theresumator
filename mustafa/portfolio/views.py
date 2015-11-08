from django.http import HttpResponse
from django.template import RequestContext, loader
from django.apps import apps

from .models import BasicInformation
from .models import Project
from .models import Experience
from .models import Language


def about(request):
    template = loader.get_template('portfolio/index.html')

    # TODO: Change used_models() work with other views
    # this is just a quick hack to check if other models like projects or education
    # have been init with objects. This will work for one view though. Chould change to work
    # with other views

    def used_models():
        """
        Checks if models other than `portfolio.models.BasicInformation`
        have atleast a single instance in db
        :return context_dict: dict containing `portfolio.models.BasicInformation` object,
                              and other models names set to True if they have
                              atleast a single instance in db
        """
        context_dict = {}
        app_models = apps.get_app_config('portfolio').get_models()
        for model in app_models:
            if model.__name__ == BasicInformation.__name__:
                context_dict[model._meta.db_table] = model.objects.get()
            else:
                if model.objects.all():
                    context_dict[model._meta.db_table] = True
        return context_dict

    context = RequestContext(request, used_models())
    return HttpResponse(template.render(context))


def projects(request):
    basic_information = BasicInformation.objects.latest('pk')
    projects_list = Project.objects.all()
    languages = Language.objects.all()
    template = loader.get_template('portfolio/projects.html')
    context = RequestContext(request, {
        'portfolio_basicinformation': basic_information,
        'portfolio_project': projects_list,
        'portfolio_experience': languages,
    })
    return HttpResponse(template.render(context))


def experience(request):
    basic_information = BasicInformation.objects.latest('pk')
    experience_list = Experience.objects.all()
    languages = Language.objects.all()
    template = loader.get_template('portfolio/experience.html')
    context = RequestContext(request, {
        'portfolio_basicinformation': basic_information,
        'portfolio_experience': experience_list,
        'portfolio_language': languages,
    })
    return HttpResponse(template.render(context))
