from django.urls import path

from Transaction.views import income_list, add_income

urlpatterns = [
    path('', income_list, name='income_list'),
    path('add-income/', add_income, name='add_incomes'),
]
