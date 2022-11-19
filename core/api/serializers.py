from rest_framework.serializers import ModelSerializer
from core.models import Actor, Card, Category, Expense, Revenue


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class RevenueSerializer(ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'

