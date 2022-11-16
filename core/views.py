from django.shortcuts import render

from utils.sumRevenues import sum_revenues
from utils.sumValues import sum_values


def index(request):
    revenue = sum_revenues()
    sum_value = sum_values()

    result = (revenue - sum_value)

    data = {
        'revenue': revenue,
        'expense': sum_value,
        'sum_value': sum_value,
        'result': result,
    }
    return render(request, 'core/index.html', data)
