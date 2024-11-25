from django.http import HttpResponse
from django.urls import path
from .views import FoodCategoryListView


def home(request):
    return HttpResponse("Добро пожаловать!")


urlpatterns = [
    path('', home, name='home'),
    path('api/v1/foods/', FoodCategoryListView.as_view(), name='food-category-list'),
]
