from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.shortcuts import redirect

from .models import Brand, TypeOfClothing, Clothes
from .forms import RegistrationForm


class MainPage(TemplateView):
    """
    Class to display main page
    """
    template_name = "clothes/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Main page"

        return context
    

class Registration(CreateView):
    """
    User registration
    """
    form_class = RegistrationForm
    template_name = "clothes/registration.html"
    success_url = reverse_lazy("authentication")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registration"
        
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect("home")
    

class Authentication(LoginView):
    """
    User Authentication
    """
    form_class = AuthenticationForm
    template_name = "clothes/authentication.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["title"] = "Authentication"

        return context
    
    def get_success_url(self):
        return reverse_lazy("home")
    

def user_logout(request):
    logout(request)
    
    return redirect("authentication")
    

class AllClothes(ListView):
    """
    Class to display all clothes
    """
    model = Clothes
    template_name = "clothes/clothes.html"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Clothes"
        
        return context
    
    def get_queryset(self):
        return Clothes.objects.select_related("type").select_related("brand")


class specificClothing(DetailView):
    """
    Class for displaying one thing
    """
    model = Clothes
    template_name = "clothes/specificClothing.html"
    slug_url_kwarg = "clothes_slug"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Clothes"

        return context
    
    def get_queryset(self):
        return Clothes.objects.filter(slug=self.kwargs[self.slug_url_kwarg]).select_related("type").select_related("brand")


class Brands(ListView):
    """
    Class to display all brands
    """
    model = Brand
    template_name = "clothes/brands.html"
    context_object_name = "brands"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Brands"

        return context
    

class ItemsByBrand(ListView):
    """
    Class for displaying clothes by brand
    """
    model = Clothes
    template_name = "clothes/brandItems.html"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Clothes"

        return context
    
    def get_queryset(self):
        return Clothes.objects.filter(brand__slug=self.kwargs["brand_slug"]).select_related("brand")
