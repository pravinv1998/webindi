
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('about/', views.about, name = "about"),
    path('services/', views.services, name = "services"),
    path('contact/', views.contact, name = "contact"),
    # path('website/', views.website, name = "website"),
    path('webapp/', views.webapp, name = "webapp"),
    path('desktopapp/', views.desktopapp, name = "desktopapp"),
    path('fetch_data/', views.fetch_data, name = "fetch_data")

]
