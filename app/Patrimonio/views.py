from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Sum
from Patrimonio.forms import ActiveForm, PassveForm

from Patrimonio.models import Active, Passive

# Create your views here.
def Home(request):
    name_template = 'patrimonio/index.html'
    actives = Active.objects.all()
    # passives = Passive.objects.all()
    
    context = {
        "actives": actives,
        "total_actives": actives.aggregate(value_t=Sum('value')),
        # "total_passives": passives.aggregate(value=Sum('value')) if passives else 0,
        "categories": [x.value for x in Active().Category],

    }
    return render(request, name_template, context)

#view crear nuevos activos
def add_active(request):
    name_template = 'patrimonio/active/new.html'
    
    if request.method == 'POST':
      form = ActiveForm(request.POST)
      if form.is_valid():
          form.save()
          redirect('add_active')
    else:
      form = ActiveForm()

    context = {
        "actives": Active.objects.all(),
        "form": form
    }
    
    return render(request, name_template, context)

#view categoria de clasificacion de activos
def filter_by_category_active(request):
    name_template = 'patrimonio/active/list_actives.html'
    filter_option = request.GET.get('filter','all')
    
    if filter_option == 'all':
        actives = Active.objects.all()
    else:
        actives = Active.objects.filter(category=filter_option)
    
    context = {
        "actives": actives,
        "categories": [x.value for x in Active().Category],

    }
    return render(request, name_template, context)

#view delete active
def delete_active(request, *args, **kwargs):
    registro = get_object_or_404(Active, pk=kwargs['pk'])
    registro.delete()
    return redirect('add_active')

#view passive
#view add passive
def add_passive(request):
    name_template = 'patrimonio/passive/new.html'
    
    if request.method == 'POST':
        form = PassveForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('add_passive')
    else:
        form = PassveForm()
    
    context = {
        "passives": Passive.objects.all(),
        "form": form
    }
    
    return render(request, name_template, context)

#view delete passive
def delete_passive(request, *args, **kwargs):
    registro = get_object_or_404(Passive, pk=kwargs['pk'])
    registro.delete()
    return redirect('add_passive')

#view categoria de clasificacion de pasivos
def filter_by_category_passive(request):
    name_template = 'patrimonio/passive/list_passives.html'
    filter_option = request.GET.get('filter','all')
    
    if filter_option == 'all':
        passives = Passive.objects.all()
    else:
        passives = Passive.objects.filter(category=filter_option)
    
    context = {
        "passives": passives,
        "categories": [x.value for x in Active().Category],

    }
    return render(request, name_template, context)
