from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'case_number', 'age', 'gender', 'chief_complaint', 'reference','contact', 'address']
        widgets = {
            'chief_complaint': forms.Textarea(attrs={'rows': 3}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()