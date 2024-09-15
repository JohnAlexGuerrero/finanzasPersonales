from django.shortcuts import render, redirect
from django.http import HttpResponse

from Transaction.models import Income, Expense
from Transaction.forms import IncomeForm, ExpenseForm

# Create your views here.
def dashboard(request):
    incomes = Income.objects.all()
    
    context = {
        'incomes': incomes,
    }
    
    return render(request, 'dashboard/index.html', context)

def add_income(request):
    # manejo del formulario
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    
    return render(request, 'income/partials/list_partial.html')

#view: expenses
def expenses_list(request):
    name_template = 'expenses/index.html'
    expenses = Expense.objects.all()
    
    context = {
        'expenses': expenses,
        'form': ExpenseForm()
    }
    
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
