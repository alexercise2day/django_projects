from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cocktail_book/', views.base, name='cocktail_book'),
    path('vodka/', views.vodka_all, name='vodka_all'),
    path('<int:pk>/', views.vodka_display, name='vodka_display'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)