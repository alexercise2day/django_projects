from django.urls import path
from . import views


urlpatterns = [
    path('cocktail_book/', views.base, name='cocktail_book'),
    path('about/', views.about, name='about'),
    path('vodka/', views.vodka_all, name='vodka_all'),
    path('vodka/vodka_display/<int:id>/', views.vodka_display, name='vodka_display'),
    path('rum/', views.rum_all, name='rum_all'),
    path('rum/rum_display/<int:id>', views.rum_display, name="rum_display"),
    path('gin/', views.gin_all, name="gin_all"),
    path('gin/gin_display/<int:id>', views.gin_display, name="gin_display"),
    path('tequila/', views.tequila_all, name="tequila_all"),
    path('tequila/tequila_display/<int:id>', views.tequila_display, name="tequila_display"),
    path('whiskey/', views.whiskey_all, name="whiskey_all"),
    path('whiskey/whiskey_display/<int:id>', views.whiskey_display, name="whiskey_display"),
] 
