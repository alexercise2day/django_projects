from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cocktails/', views.cocktails, name='cocktails'),
    path('', views.base, name='base'),
    path('vodka/', views.vodka, name='vodka'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)