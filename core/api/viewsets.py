from rest_framework.viewsets import ModelViewSet
from core.models import Actor, Card, Category, Expense, Revenue
from .serializers import ActorSerializer, CardSerializer, CategorySerializer, ExpenseSerializer, RevenueSerializer


class ActorViewset(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CardViewset(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewset(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class RevenueViewset(ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer