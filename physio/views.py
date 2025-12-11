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