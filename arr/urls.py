from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('categories/<int:pk>/', views.home, name='home'),
    path('category_page/<int:pk>/', views.category_page, name='theme'),
    path('theme_page/<int:pk>/', views.theme_page, name='theme_page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)