from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def blog_grid(request):
    return render(request, 'blog_grid.html')

def blog_detail(request):
    return render(request, 'blog_detail.html')

def pricing(request):
    return render(request, 'pricing.html')

def features(request):
    return render(request, 'features.html')

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def quote(request):
    return render(request, 'quote.html')

def contact(request):
    return render(request, 'contact.html')
