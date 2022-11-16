

from datetime import date
from core.models import Expense


def sum_values():
    current_date = date.today()
    expense = Expense.objects.all()
    sum_value = 0
    for i in expense:
        if (i.start_date.strftime('%Y/%m') <= current_date.strftime('%Y/%m') <=
                i.end_date.strftime('%Y/%m') or i.fixed_expense):
            if i.installment_plan > 0:
                sum_value += i.installment_amount
            else:
                sum_value += i.value
    return sum_value