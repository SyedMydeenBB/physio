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


    path('dashboard/', views.dashboard, name='dashboard'),


     path('daily_sheet_list/', views.daily_sheet_list, name='daily_sheet_list'),
    path('daily_sheet_create/', views.daily_sheet_create, name='daily_sheet_create'),
    path('daily_sheet_update/<int:pk>/', views.daily_sheet_update, name='daily_sheet_update'),
    path('daily_sheet_delete/<int:pk>/', views.daily_sheet_delete, name='daily_sheet_delete'),
    path('export/', views.daily_sheet_export, name='daily_sheet_export'),
    path('import/', views.daily_sheet_import, name='daily_sheet_import'),

]