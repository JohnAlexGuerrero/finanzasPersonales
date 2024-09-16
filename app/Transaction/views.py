from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db.models import Value
from django.db.models.functions import Concat

from Transaction.models import Income, Expense
from Transaction.forms import IncomeForm, ExpenseForm

# Create your views here.
def transactions_list(request):
    name_template = 'transactions/partials/list_partial.html'
    
    incomes = Income.objects.annotate(
        category=Value('Ingreso')
    ).values('description','value','created','type','category')
    expenses = Expense.objects.annotate(
        category=Value('Gasto')
    ).values('description','value','created','type','category')
    
    transactions = expenses.union(incomes).order_by('-created')
    
    context = {
        'transactions': transactions,
    }
    
    return render(request, name_template, context)

def dashboard(request):
    name_template = 'dashboard/index.html'
    
    return render(request, name_template)

def add_income(request):
    # manejo del formulario
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    
    return render(request, 'income/partials/list_partial.html')

def incomes_list(request):
    name_template = 'income/partials/list_partial.html'
    incomes = Income.objects.annotate(
        category=Value('Ingreso')
    ).values('description','value','created','type','category')
    
    context = {
        'incomes': incomes,
    }
    
    return render(request, name_template, context)

#view: expenses
def expenses_list(request):
    name_template = 'expenses/partials/list_partial.html'
    expenses = Expense.objects.annotate(
        category=Value('Gasto')
    ).values('description','value','created','type','category')
    
    context = {
        'expenses': expenses
    }
    
    return render(request, name_template, context)

#view statistics of expenses
def statistics_expenses(request):
    context = {}
    name_template = 'expenses/partials/statistics.html'
    expenses = Expense.objects.all().order_by('type')
    context['categories'] = [x.category() for x in expenses]
    print(context)
    
    return render(request, name_template, context)

def add_expense(request):
    name_template = 'expense/new.html'
    # manejo del formulario
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses_list')
    
    return render(request, name_template)
