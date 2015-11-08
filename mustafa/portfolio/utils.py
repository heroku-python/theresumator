from django.apps import apps


def used_models(context_dict):
        """
        Checks if models other than whats in `context_dict`
        have atleast a single instance in db
        :return context_dict: dict containing already assigned objects,
                              and other models names value set to True
                              if they have atleast a single instance in db
        """
        app_models = apps.get_app_config('portfolio').get_models()
        for model in app_models:
            if model._meta.db_table in context_dict:
                pass
            else:
                if model.objects.all():
                    context_dict[model._meta.db_table] = True
        return context_dict
