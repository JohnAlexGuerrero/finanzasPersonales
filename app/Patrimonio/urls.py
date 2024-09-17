from django.urls import path

from Patrimonio.views import Home, add_active, filter_by_category_active

urlpatterns = [
    path('', Home, name='index'),
    path('actives/add/', add_active, name='add_active'),
    path('actives/category', filter_by_category_active, name='filter_by_category_active'),
]
