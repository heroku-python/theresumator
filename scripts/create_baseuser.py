from django.db.utils import OperationalError
from solo.admin import SingletonModelAdmin

from resumator.models import BasicInformation


# make BasicInformation singleton if it does not already exist
try:
    basic_information = BasicInformation.get_solo()
except OperationalError:
    pass
