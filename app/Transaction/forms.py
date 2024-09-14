from django import forms

from Transaction.models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['description','value','type']
    
