from django.shortcuts import render
from .models import Category, Theme


def home(request):
    categ = Category.objects.all()
    theme010 = Theme.objects.all()
    return render(request, 'home.html', {'categ': categ, 'theme010': theme010})


def category_page(request, pk):
    categ1 = Category.objects.get(id=pk)
    themes = Theme.objects.filter(theme_category_id=pk)
    return render(request, 'category.html', {'categ1': categ1, 'themes': themes})

def theme_page(request, pk):
    themes1 = Theme.objects.get(id=pk)
    return render(request, 'Themes.html', {'themes1': themes1})