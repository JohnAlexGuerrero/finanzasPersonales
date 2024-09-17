from django import forms

from Patrimonio.models import Active

class ActiveForm(forms.ModelForm):
    
    class Meta:
        model = Active
        fields = ("description","value","is_fijo","category","type","created")
        
        widgets = {
            "created": forms.DateInput(attrs={"type":"date"})
        }
