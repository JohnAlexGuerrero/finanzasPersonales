from django.urls import path

# from Transaction.views import incomes_list, transactions_list, expense_delete, income_delete
# from Transaction.views import dashboard, add_income, expenses_list, add_expense, statistics_expenses
from Transaction.views import home_expenses, add_expense

urlpatterns = [
    # path('', dashboard, name='dashboard'),
    
    path('expenses/', home_expenses, name='home_expenses'),
    path('add-expense/', add_expense, name='add_expenses'),
    
    # path('expenses/statistics/', statistics_expenses, name='expenses_statistics'),
    # path('transactions/', transactions_list, name='transactions_list'),
    # path('expenses/', expenses_list, name='expenses_list'),
    # path('expenses/<int:pk>/delete/', expense_delete, name='expenses_delete'),
    # path('incomes/', incomes_list, name='incomes_list'),
    # path('incomes/<int:pk>/delete/', income_delete, name='incomes_delete'),
    # path('add-income/', add_income, name='add_incomes'),
]
