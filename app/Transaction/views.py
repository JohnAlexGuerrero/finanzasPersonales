from django.shortcuts import render, redirect
from django.http import HttpResponse

from Transaction.models import Income
from Transaction.forms import IncomeForm

# Create your views here.
def income_list(request):
    incomes = Income.objects.all()
    
    # manejo del formulario
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    
    context = {
        'incomes': incomes,
        'form': form
    }
    return render(request, 'income/list.html', context)

def add_income(request):
    pass
    #     return render(request, 'income/partials/list_partial.html',{'incomes':incomes})
    # return HttpResponse(status=400)