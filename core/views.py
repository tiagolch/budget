from django.shortcuts import render

from utils.sumRevenues import sum_revenues
from utils.sumValues import sum_values
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Revenue


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


class RevenueListView(ListView):
    model = Revenue


class RevenueDetailView(DetailView):
    context_object_name = 'revenue'
    queryset = Revenue.objects.all()

