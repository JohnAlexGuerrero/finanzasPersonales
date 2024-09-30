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

#view home incomes
def home_incomes(request):
    template_name = 'income/index.html'
    dates = []
    form = IncomeForm
    incomes = get_incomes_list().order_by('-created')
    dates = set([x.created for x in incomes])
    
    context = {
        "form": form,
        "dates": sorted(dates, reverse=True),
        "incomes": incomes
    }   
    
    return render(request, template_name, context)

#function for list incomes
def get_incomes_list():
    return Income.objects.all()
    
#view contiene el formulario de creacion de un nuevo ingreso y su lista
def add_income(request):
    name_template = 'income/index.html'
    # manejo del formulario
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, name_template)
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

#function: get_object_expenses
def get_object_expenses():
    expenses = Expense.objects.all().order_by('-created')
    dates = set([d.created for d in expenses])
    return expenses, sorted(dates, reverse=True)

#view home of expenses
def home_expenses(request):
    template_name = 'expenses/index.html'
    
    form = ExpenseForm()
    expenses, dates = get_object_expenses()
    
    
    context = {
        "expenses": expenses,
        "dates": dates,
        "statistics": [
                {
                    "name": exp.type,
                    "total": exp.total_value(), 
                    "count": exp.count(),
                    "mean": exp.mean(),
                    "min": 0,
                    "max": exp.max_value(),
                    "25%":0,
                    "50%":0,
                    "percentile75": exp.perc_75(),
                }
                for exp in expenses
            ],
        # "categories": [c for c in expenses.order_by('type')], #statistics_expenses(expenses),
        "form": form
    }
    
    return render(request, template_name, context)

#view delete expenses
def expense_delete(request, *args, **kwargs):
    name_template = 'expenses/partials/list.html'

    registro = get_object_or_404(Expense, pk=kwargs['pk'])
    registro.delete()
    expenses, dates = get_object_expenses()
    
    context = {
        "expenses": expenses,
        "dates": dates,
    }
    
    return render(request, name_template, context)
    
#function statistics of expenses
def statistics_expenses(type_name):
    return Expense.objects.filter(type=type_name).first()
    
#view para agregar un nuevo gasto
def add_expense(request):
    name_template = 'expenses/partials/list.html'
    # manejo del formulario
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            expenses, dates = get_object_expenses()
            
            context = {
                'expenses': expenses,
                'dates': dates,
            }
            
            return render(request, name_template, context)
        
#funcion que devuelve la informacion guardad en DB del modelo ingreso
def get_object_incomes():
    incomes = Income.objects.annotate(
        category=Value('Ingreso')
    ).values('id','description','value','created','type','category')
    return incomes

#function que devuelve la informacion guardada en DB del modelo gastos
# def get_object_expenses():
#     expenses = Expense.objects.annotate(
#         category=Value('Gasto')
#     ).values('id','description','value','created','type','category')
#     return expenses