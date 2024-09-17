from django.shortcuts import render, redirect

from Patrimonio.forms import ActiveForm

from Patrimonio.models import Active

# Create your views here.
def Home(request):
    name_template = 'patrimonio/index.html'
    context = {
        "actives": Active.objects.all(),
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