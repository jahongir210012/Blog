from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
        path('registration', registration, name='registration'),
        path('login', login, name='login'),
        path('about/', about_us, name='about_us'),
        path('contact-us/', contact_us, name='contact_us'),
        path('testimonial/', testimonial, name='testimonial'),
        path('our-protein/', our_protein, name='our_protein'),
]