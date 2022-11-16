

from core.models import Revenue
from django.db.models import Sum


def sum_revenues():
    return Revenue.objects.all().aggregate(Sum('value'))['value__sum']
