from typing import Any
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import *
from .get_articles import *
from .models import *
from .parser import *
from .utils import SearchView
from django.contrib.auth import logout, login


def home(request):
    return render(request, 'newsapp/index.html', context={'title': 'bebra.site'})


def headlines(request):
    return render(request, 'newsapp/top-headlines.html')


def everything(request):
    return render(request, 'newsapp/everything.html')


class ShowArticles(ListView):
    paginate_by = 8
    template_name = 'newsapp/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(user=self.request.user)


class HeadlineSerch(SearchView):
    template_name = 'newsapp/search_results.html'
    api_url = "https://newsapi.org/v2/top-headlines?apikey="


class EverythingSearch(SearchView):
    template_name = 'newsapp/everything_results.html'
    api_url = "https://newsapi.org/v2/everything?apikey="


class RegUser(CreateView):
    form_class = RegUserForm
    template_name = 'newsapp/reg.html'
    success_url = 'https://www.youtube.com/watch?v=9ND_kN7ecHQ&list=LL&index=1'
    

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_url')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'newsapp/login.html'

    def get_success_url(self):
        return reverse_lazy('home_url')

def logout_user(request):
    logout(request)
    return redirect('login_url')
