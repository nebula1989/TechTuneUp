from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('repair_services/', views.repair_services, name='repair_services'),
    path('pricing_tables/', views.pricing_tables, name='pricing_tables'),
    path('team/', views.team, name='team'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('faq/', views.faq, name='faq'),
]