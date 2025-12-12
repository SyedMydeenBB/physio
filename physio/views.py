from django.shortcuts import render

def index(request):
    """Home page view"""
    context = {
        'title': 'CHENNAI PHYSIO CARE - For a Better Quality of Life',
        'phone': '+91-73052-74514',
        'email': 'admin@chennaiphysiocare.com',
        'address': '2, Pearl Apartments, 13th Main Rd, Anna Nagar West, Chennai, Tamil Nadu 600040',
        'years_experience': '20+',
        'patients_served': '25K+',
        'recovery_rate': '99.9%',
    }
    return render(request, 'physio/index.html', context)

def services(request):
    """Services page view"""
    context = {
        'title': 'Our Services - Chennai Physio Care',
    }
    return render(request, 'physio/services.html', context)

def contact(request):
    """Contact page view"""
    context = {
        'title': 'Contact Us - Chennai Physio Care',
    }
    return render(request, 'physio/contact.html', context)

def blog(request):
    """Blog page view"""
    context = {
        'title': 'Blog - Chennai Physio Care',
    }
    return render(request, 'physio/blog.html', context)

def guide(request):
    """Guide page view"""
    context = {
        'title': 'Patient Guide - Chennai Physio Care',
    }
    return render(request, 'physio/guide.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Us - Chennai Physio Care',
    }
    return render(request, 'physio/about.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Patient
from .forms import PatientForm, UploadFileForm
import pandas as pd
from io import BytesIO

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})

def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_confirm_delete.html', {'patient': patient})

def upload_excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)

            # Normalize headers
            df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

            for _, row in df.iterrows():
                Patient.objects.update_or_create(
                    case_number=row.get('case_number'),
                    defaults={
                        'name': row.get('name'),
                        'age': row.get('age'),
                        'gender': row.get('gender'),
                        'chief_complaint': row.get('chief_complaint'),
                        'reference': row.get('reference'),
                        'contact': row.get('contact_number') or row.get('contact'),
                        'address': row.get('address')
                    }
                )
            return redirect('patient_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload_excel.html', {'form': form})


def download_excel(request):
    patients = Patient.objects.all()
    data = {
        'Name': [p.name for p in patients],
        'Case Number': [p.case_number for p in patients],
        'Age': [p.age for p in patients],
        'Gender': [p.get_gender_display() for p in patients],
        'Chief Complaint': [p.chief_complaint for p in patients],
        'Reference': [p.reference for p in patients],
        'Contact': [p.contact for p in patients],
        'Address': [p.address for p in patients],
    }
    
    df = pd.DataFrame(data)
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=patients.xlsx'
    return response