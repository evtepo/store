from django.urls import path

from .views import MainPage, AllBrands, SingleBrand


urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("brands/", AllBrands.as_view(), name="brands"),
    path("brands/type/<slug:brand_slug>/", SingleBrand.as_view(), name="type"),
]
