from django import forms

from Transaction.models import Income, Expense

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['description','value','type']
    

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description','value','type','way_to_pay']
    
