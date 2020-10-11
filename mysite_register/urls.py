from django.urls import path
from .views import HomeView, home

urlpatterns = [
    path('', HomeView.as_view(), name = 'mysite-home'),
    path('all/', home, name = 'home')
]