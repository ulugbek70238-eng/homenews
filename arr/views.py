from django.shortcuts import render
from .models import Category, Theme


def home(request):
    categ = Category.objects.all()
    return render(request, 'home.html', {'categ': categ})

def category_page(request, pk):
    themes = Theme.objects.filter(theme_category_id=pk)
    return render(request, 'Category.html', {'themes': themes})

def theme_page(request, pk):
    themes1 = Theme.objects.get(id=pk)
    return render(request, 'Themes.html', {'themes1': themes1})