from django.urls import path, include
from .views import HomePageView, AboutPageView, ContactCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactCreateView.as_view(), name='contact'),
]