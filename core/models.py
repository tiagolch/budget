from django.db import models
from datetime import date, timedelta


class Budget(models.Model):
    description = models.CharField(max_length=100)
    value = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    obs = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description


class Revenue(Budget):
    name = models.ForeignKey(
        'Actor', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.description}'


class Expense(Budget):
    name = models.ForeignKey(
        'Actor', on_delete=models.CASCADE, blank=True, null=True)
    card = models.ForeignKey(
        'Card', on_delete=models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=True, null=True)
    installment_plan = models.PositiveIntegerField(blank=True, default=0)
    installment_amount = models.DecimalField(
        default=0, blank=True, max_digits=10, decimal_places=2)
    start_date = models.DateField(blank=True, default=date.today())
    end_date = models.DateField(blank=True, null=True)
    fixed_expense = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description

    def save(self, *args, **kwargs):
        if self.installment_plan > 0:
            temp = self.start_date
            temp += timedelta(days=((self.installment_plan - 1) * 30))
            self.end_date = temp
            self.installment_amount = (self.value / self.installment_plan)
        else:
            self.end_date = self.start_date
            self.installment_amount = self.value
        super(Expense, self).save(*args, **kwargs)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=25)
    number = models.PositiveIntegerField(blank=True, null=True)
    obs = models.TextField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description