from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('categories/<int:pk>', views.home, name='home'),
    path('themes/<int:pk>/', views.category_page, name='theme_page'),
]