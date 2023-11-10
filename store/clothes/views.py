from django.views.generic import ListView, TemplateView, DetailView

from .models import Brand, TypeOfClothing


class MainPage(TemplateView):
    template_name = "clothes/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Main page"

        return context


class AllBrands(ListView):
    model = Brand
    template_name = "clothes/brands.html"
    context_object_name = "brands"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Brands"

        return context


class SingleBrand(ListView):
    model = TypeOfClothing
    template_name = "clothes/type.html"
    context_object_name = "type"
    slug_url_kwarg = "brand_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs[self.slug_url_kwarg])

        return context

    def get_queryset(self):
        return TypeOfClothing.objects.filter(brands__slug=self.kwargs[self.slug_url_kwarg]).prefetch_related("brands").all()
