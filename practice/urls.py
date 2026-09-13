from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('advisory/', views.advisory, name='advisory'),
    path('advisory/<slug:slug>/', views.service_detail, name='service_detail'),
    path('engagement/<slug:slug>/', views.engagement_detail, name='engagement_detail'),
    path('experience/', views.experience, name='experience'),
    path('credentials/', views.credentials, name='credentials'),
    path('method/', views.method, name='method'),
    path('contact/', views.contact, name='contact'),
]
