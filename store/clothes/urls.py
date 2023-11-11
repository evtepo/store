from django.urls import path

from .views import MainPage, AllClothes, specificClothing, Brands, ItemsByBrand


urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("clothes/", AllClothes.as_view(), name="clothes"),
    path("clothes/<slug:clothes_slug>", specificClothing.as_view(), name="specificClothing"),
    path("brands", Brands.as_view(), name="brands"),
    path("brands/<slug:brand_slug>", ItemsByBrand.as_view(), name="brandItems")
]
