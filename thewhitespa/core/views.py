from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Testimonial, TeamMember, GalleryImage, BusinessHour
from .forms import BookingForm


BUSINESS_INFO = {
    'name': 'The White Spa',
    'address': 'Rue Tantan (à côté de Sky17), Tangier, Morocco',
    'phone': '+212 678-046529',
    'category': 'Spa & Wellness',
    'latitude': 35.7743157,
    'longitude': -5.7936762,
}


def home(request):
    featured_services = Service.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)[:4]
    team_members = TeamMember.objects.all()[:4]
    context = {
        'featured_services': featured_services,
        'testimonials': testimonials,
        'team_members': team_members,
        'business': BUSINESS_INFO,
    }
    return render(request, 'core/home.html', context)


def services(request):
    from collections import OrderedDict
    categories = Service.CATEGORY_CHOICES
    services_by_category = OrderedDict()
    for code, label in categories:
        qs = Service.objects.filter(category=code)
        if qs.exists():
            services_by_category[label] = qs
    context = {
        'services_by_category': services_by_category,
        'business': BUSINESS_INFO,
    }
    return render(request, 'core/services.html', context)


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Votre réservation a été envoyée avec succès ! '
                'Nous vous contacterons pour confirmer votre rendez-vous.',
            )
            return redirect('booking')
    else:
        form = BookingForm()
    context = {
        'form': form,
        'services': Service.objects.all(),
        'business': BUSINESS_INFO,
    }
    return render(request, 'core/booking.html', context)


def about(request):
    team_members = TeamMember.objects.all()
    gallery_images = GalleryImage.objects.all()
    context = {
        'team_members': team_members,
        'gallery_images': gallery_images,
        'business': BUSINESS_INFO,
    }
    return render(request, 'core/about.html', context)


def contact(request):
    business_hours = BusinessHour.objects.all()
    context = {
        'business_hours': business_hours,
        'business': BUSINESS_INFO,
        'google_maps_embed': (
            'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3236.0!2d-5.7936762'
            '!3d35.7743157!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0'
            '!2sThe+White+Spa!5e0!3m2!1sfr!2sma!4v1'
        ),
    }
    return render(request, 'core/contact.html', context)
