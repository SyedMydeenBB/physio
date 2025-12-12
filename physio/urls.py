from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('guide/', views.guide, name='guide'),
    path('about/', views.about, name='about'),

    path('patient_list/', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('edit/<int:pk>/', views.patient_edit, name='patient_edit'),
    path('delete/<int:pk>/', views.patient_delete, name='patient_delete'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('download/', views.download_excel, name='download_excel'),
]