from django.urls import path

from Transaction.views import dashboard, add_income, expenses_list, add_expense

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('expenses/', expenses_list, name='expenses_list'),
    path('add-income/', add_income, name='add_incomes'),
    path('add-expense/', add_expense, name='add_expenses'),
]
