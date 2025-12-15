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


from .models import DailySheet

class DailySheetForm(forms.ModelForm):
    class Meta:
        model = DailySheet
        fields = [
            'date', 'name', 'case_number', 'diagnosis', 'charge', 'received',
            'payment_status', 'payment_type', 'payment_frequency',
            'in_time', 'out_time', 'treatment_1', 'treatment_2',
            'treatment_3', 'treatment_4', 'therapist_1', 'therapist_2'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
            'case_number': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'received': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'payment_status': forms.Select(attrs={'class': 'form-control', 'id': 'id_payment_status'}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'payment_frequency': forms.Select(attrs={'class': 'form-control'}),
            'in_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'id': 'id_in_time'}),
            'out_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'id': 'id_out_time'}),
            'treatment_1': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'treatment_2': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'treatment_3': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'treatment_4': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'therapist_1': forms.Select(attrs={'class': 'form-control'}),
            'therapist_2': forms.Select(attrs={'class': 'form-control'}),
        }

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(
        label='Upload Excel File',
        help_text='Upload an Excel file (.xlsx, .xls)',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.xlsx,.xls'})
    )
