from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('categories/<int:pk>/', views.home, name='home'),
    path('category_page/<int:pk>/', views.category_page, name='theme'),
    path('theme_page/<int:pk>/', views.theme_page, name='theme_page'),
]