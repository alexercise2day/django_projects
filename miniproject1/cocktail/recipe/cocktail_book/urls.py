from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.base, name='home'),
    path('vodka/', views.vodka, name='vodka'),
    path('<int:pk>/', views.vodka_display, name='vodka_display'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)