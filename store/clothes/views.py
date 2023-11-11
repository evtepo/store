from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, TemplateView, DetailView

from .models import Brand, TypeOfClothing, Clothes


class MainPage(TemplateView):
    template_name = "clothes/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Main page"

        return context
    

class AllClothes(ListView):
    model = Clothes
    template_name = "clothes/clothes.html"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Clothes"
        
        return context
    
    def get_queryset(self):
        return Clothes.objects.select_related("type").select_related("brand")


class specificClothing(DetailView):
    model = Clothes
    template_name = "clothes/specificClothing.html"
    slug_url_kwarg = "clothes_slug"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_queryset(self):
        return Clothes.objects.filter(slug=self.kwargs[self.slug_url_kwarg]).select_related("type").select_related("brand")


class Brands(ListView):
    model = Brand
    template_name = "clothes/brands.html"
    context_object_name = "brands"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Brands"

        return context
    

class ItemsByBrand(ListView):
    model = Clothes
    template_name = "clothes/brandItems.html"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def get_queryset(self):
        return Clothes.objects.filter(brand__slug=self.kwargs["brand_slug"]).select_related("brand")
