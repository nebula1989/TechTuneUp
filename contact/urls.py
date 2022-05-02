from django.urls import path, include
from contact import views as contact_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('contact', contact_views.contact_under_construction, name='contact'),
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
