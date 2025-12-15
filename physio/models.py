from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    name = models.CharField(max_length=100, blank=True, null=True)
    case_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    chief_complaint = models.TextField(blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.case_number}"
    


from django.db import models
from django.utils import timezone

class DailySheet(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('partially_paid', 'Partially Paid'),
        ('not_paid', 'Not Paid'),
    ]
    
    PAYMENT_TYPE_CHOICES = [
        ('qr', 'QR'),
        ('cash', 'Cash'),
    ]
    
    PAYMENT_FREQUENCY_CHOICES = [
        ('daily', 'Daily Basis'),
        ('weekly', 'Weekly Basis'),
        ('monthly', 'Monthly Basis'),
    ]
    
    THERAPIST_CHOICES = [
        ('dr_basidh', 'Dr. Basidh'),
        ('dr_visitra', 'Dr. Visitra'),
        ('dr_bharatiselvi', 'Dr. Bharatiselvi'),
    ]
    
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=200)
    case_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    diagnosis = models.TextField()
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    received = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES)
    payment_frequency = models.CharField(max_length=20, choices=PAYMENT_FREQUENCY_CHOICES)
    in_time = models.TimeField(null=True, blank=True)
    out_time = models.TimeField(null=True, blank=True)
    treatment_1 = models.TextField(blank=True)
    treatment_2 = models.TextField(blank=True)
    treatment_3 = models.TextField(blank=True)
    treatment_4 = models.TextField(blank=True)
    therapist_1 = models.CharField(max_length=20, choices=THERAPIST_CHOICES)
    therapist_2 = models.CharField(max_length=20, choices=THERAPIST_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.case_number} - {self.date}"
