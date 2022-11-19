from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from core.views import index
from core.api.viewsets import ActorViewset, CardViewset, CategoryViewset, ExpenseViewset, RevenueViewset


routers = routers.DefaultRouter()

routers.register(r'actor/', ActorViewset, basename='actor')
routers.register(r'card/', CardViewset, basename='card')
routers.register(r'category/', CategoryViewset, basename='category')
routers.register(r'expense/', ExpenseViewset, basename='expense')
routers.register(r'revenue/', RevenueViewset, basename='revenue')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include(routers.urls)),

]
