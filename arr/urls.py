from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('category/<int:pk>/', views.theme_page, name='theme_page'),
]