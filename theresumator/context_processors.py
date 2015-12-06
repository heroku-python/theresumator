from django.apps import apps
from resumator.models import BasicInformation


def used_models(context_dict):
        """
        Checks if models other than whats in `context_dict` or `ignore_models`
        have atleast a single instance in db
        :return context_dict: dict containing already assigned objects.
                              sets models names as key and value set to True
                              if they have atleast a single instance in db.
                              Ignores models in `ignore_models`
        """
        basic_information = BasicInformation.objects.get()
        context_dict["resumator_basicinformation"] = basic_information

        checked_apps = ['resumator', 'andablog']

        for app in checked_apps:
            app_models = apps.get_app_config(app).get_models()
            for model in app_models:
                    if model.objects.all():
                        key = "".join(["is_", model._meta.db_table])
                        context_dict[key] = True

        return context_dict


def global_item(request):
    '''
    A context processor to add the django-resumator's items to the current Context
    '''
    return used_models({})
