from django.shortcuts import render

from django.shortcuts import render
from .models import *

def home(request):
    context= {}
    template_name = 'index.html'
    carousel_items = CarouselItem.objects.all()
    facts = Fact.objects.all()
    team_members = TeamMember.objects.all()
    faqs = FAQ.objects.all()
    testimonials = Testimonial.objects.all()

    context['testimonials'] = testimonials
    context['faqs'] = faqs
    context['team_members'] = team_members
    context['carousel_items'] = carousel_items
    context['facts'] = facts
    
    return render(request, template_name, context)

def about(request):
    context= {}
    template_name = 'about.html'
    
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()
    
    context['testimonials'] = testimonials
    context['team_members'] = team_members
    return render(request, template_name, context)

def services(request):
    context = {}
    testimonials = Testimonial.objects.all()
    
    context['testimonials'] = testimonials
    return render(request, 'service.html', context)

def blog_grid(request):
    return render(request, 'blog_grid.html')

def blog_detail(request):
    return render(request, 'blog_detail.html')

def pricing(request):
    return render(request, 'pricing.html')

def features(request):
    return render(request, 'features.html')

def teams(request):
    team_members = TeamMember.objects.all()  # Fetch all team members
    return render(request, 'team.html', {'team_members': team_members})

    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def quote(request):
    return render(request, 'quote.html')

def contact(request):
    return render(request, 'contact.html')
