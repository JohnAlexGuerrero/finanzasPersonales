from django.urls import path

from Patrimonio.views import Home, add_active, filter_by_category_active, delete_active, add_passive, delete_passive, filter_by_category_passive

urlpatterns = [
    path('', Home, name='index'),
    path('actives/add/', add_active, name='add_active'),
    path('passives/add/', add_passive, name='add_passive'),
    path('actives/<int:pk>/delete/', delete_active, name='delete_active'),
    path('passives/category', filter_by_category_passive, name='filter_by_category_passive'),
    path('passives/<int:pk>/delete/', delete_passive, name='delete_passive'),
    path('actives/category', filter_by_category_active, name='filter_by_category_active'),
]
