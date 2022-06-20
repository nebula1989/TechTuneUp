from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('repair_services/', views.repair_services, name='repair_services'),
    path('tech_services/', views.tech_services, name='tech_services'),
    path('repair_services/laptop_repair', views.laptop_repair, name='laptop_repair'),
    path('pricing_tables/', views.pricing_tables, name='pricing_tables'),
    path('team/', views.team, name='team'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('faq/', views.faq, name='faq'),
]