from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('all_services/', views.all_services, name='all_services'),
    path('repair_services/', views.repair_services, name='repair_services'),
    path('repair_services/pc/', views.pc_repair, name='pc_repair'),
    path('repair_services/mobile/', views.mobile_repair, name='mobile_repair'),
    path('repair_services/tablet/', views.tablet_repair, name='tablet_repair'),
    path('repair_services/gaming/', views.gaming_repair, name='gaming_repair'),

    path('tech_services/', views.tech_services, name='tech_services'),
    path('tech_services/app_dev', views.app_dev, name='app_dev'),
    path('pricing_tables/', views.pricing_tables, name='pricing_tables'),
    path('team/', views.team, name='team'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('faq/', views.faq, name='faq'),
]