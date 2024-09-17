from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.db.models import Value
from django.db.models.functions import Concat

from Transaction.models import Income, Expense
from Transaction.forms import IncomeForm, ExpenseForm

# View para mostrar las transacciones(ingresos, gastos) guardadas
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

#view muestra el resument de todas los modelos creados
def dashboard(request):
    name_template = 'dashboard/index.html'
    
    return render(request, name_template)

#view contiene el formulario de creacion de un nuevo ingreso y su lista
def add_income(request):
    name_template = 'income/new.html'
    # manejo del formulario
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_incomes')
    else:
        form = IncomeForm()
    
    context = {
        'form': form,
        'incomes': get_object_incomes().order_by('-created')
    }
    
    return render(request, name_template, context)

#view muestra una lista de ingresos
def incomes_list(request):
    name_template = 'income/partials/list_partial.html'
    incomes = get_object_incomes().order_by('-created')
    
    context = {
        'incomes': incomes,
    }
    
    return render(request, name_template, context)

#view delete income
def income_delete(request, *args, **kwargs):
    income = get_object_or_404(Income, pk=kwargs['pk'])
    income.delete()
    context = {'mensaje': 'Registro eliminado correctamente'}
    return redirect('add_incomes')

#views expenses
#view: muestra una lista de gastos
def expenses_list(request):
    name_template = 'expenses/partials/list_partial.html'
    
    context = {
        'expenses': get_object_expenses().order_by('-created')
    }
    
    return render(request, name_template, context)

#view delete expenses
def expense_delete(request, *args, **kwargs):
    registro = get_object_or_404(Expense, pk=kwargs['pk'])
    registro.delete()
    context = {'mensaje': 'Registro eliminado correctamente'}
    return redirect('add_expenses')
    
#view statistics of expenses
def statistics_expenses(request):
    context = {}
    name_template = 'expenses/partials/statistics.html'
    expenses = Expense.objects.all().order_by('type')
    context['categories'] = [x.category() for x in expenses]
    
    return render(request, name_template, context)

#view para agregar un nuevo gasto
def add_expense(request):
    name_template = 'expenses/new.html'
    # manejo del formulario
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_expenses')
    else:
        form = ExpenseForm()
    
    context = {
        'form':form,
        'expenses': get_object_expenses().order_by('-created')
    }
        
    return render(request, name_template, context)

#funcion que devuelve la informacion guardad en DB del modelo ingreso
def get_object_incomes():
    incomes = Income.objects.annotate(
        category=Value('Ingreso')
    ).values('id','description','value','created','type','category')
    return incomes

#function que devuelve la informacion guardada en DB del modelo gastos
def get_object_expenses():
    expenses = Expense.objects.annotate(
        category=Value('Gasto')
    ).values('id','description','value','created','type','category')
    return expenses