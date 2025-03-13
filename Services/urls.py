from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'), 
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonial, name='testimonials'),
    path('pricing/', views.pricing, name='pricing'),
    path('portfoliodetails/',views.portfoliodetails,name='portfoliodetails'),
    path('servicedetails/',views.servicedetails,name='servicedetails'),
    path('blogdetails/', views.blogdetails, name='blogdetails')
]