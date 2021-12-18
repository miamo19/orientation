from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login', login, name='login'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('course', course, name='course'),
    path('event', event, name='event'),

]
