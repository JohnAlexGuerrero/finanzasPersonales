from django.urls import path

from Transaction.views import dashboard, add_income, expenses_list, add_expense, statistics_expenses, incomes_list, transactions_list, expense_delete

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('expenses/statistics/', statistics_expenses, name='expenses_statistics'),
    path('transactions/', transactions_list, name='transactions_list'),
    path('expenses/', expenses_list, name='expenses_list'),
    path('expenses/<int:pk>/delete/', expense_delete, name='expenses_delete'),
    path('incomes/', incomes_list, name='incomes_list'),
    path('add-income/', add_income, name='add_incomes'),
    path('add-expense/', add_expense, name='add_expenses'),
]
