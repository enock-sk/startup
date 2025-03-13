from django.shortcuts import render

from Services.models import PortfolioItems

# Create your views here.

def index(request):
    items=PortfolioItems.objects.all()
    context={'items': items}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request,'services.html', {})

def servicedetails(request):
    return render(request,'service-details.html')

def portfolio(request):
    return render(request, 'portfolio.html', {})

def portfoliodetails(request):
    return render(request, 'portfolio-details.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogdetails(request):
    return render(request, 'blog-details.html')

def contact(request):
    return render(request, 'contact.html', {})

def team(request):
    return render(request, 'team.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def testimonial(request):
    return render(request, 'testimonials.html', {})