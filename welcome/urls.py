from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('repair', views.repair_services, name='repair_services'),
    path('repair/pc/', views.pc_repair, name='pc_repair'),
    path('repair/mobile/', views.mobile_repair, name='mobile_repair'),
    path('repair/tablet/', views.tablet_repair, name='tablet_repair'),
    path('repair/game-console/', views.gaming_repair, name='gaming_repair'),

    path('tech_services/', views.tech_services, name='tech_services'),
    path('website-development', views.app_dev, name='app_dev'),
    path('team/', views.team, name='team'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('faq/', views.faq, name='faq'),
]