from django.shortcuts import render
from .models import Category, Theme


def home(request):
    categ = Category.objects.all()
    return render(request, 'home.html', {'categ': categ})

def category_page(request, pk):
    themes = Theme.objects.all()
    return render(request, 'category.html', {'themes': themes})