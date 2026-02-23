from django.shortcuts import render
from .models import Category, Theme
# Create your views here.

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_page(request, pk):
    categori = Category.objects.all(id=pk)
    themes = Theme.objects.all()
    return render(request, 'category.html', {'categori': categori, 'themes': themes})

