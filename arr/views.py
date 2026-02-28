from django.shortcuts import render, redirect
from .models import Category, Theme
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login, logout
from .forms import RegForm
from django.views import View

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

def Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = RegForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            email = form.cleaned_data('email')
            password = form.cleaned_data('password1')


            user = User.object.create_user(username=username,
                                           email=email,
                                           password=password)
            user.save()
            login(request, user)
            return redirect('/')

def search(request):
    if request.method == 'POST':
        search_product = request.POST.get['search_product']
