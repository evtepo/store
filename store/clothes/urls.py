from django.urls import path

from .views import (MainPage, AllClothes, specificClothing,
                    Brands, ItemsByBrand, Registration, Authentication,
                    user_logout,)


urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("authentication/", Authentication.as_view(), name="authentication"),
    path("logout/", user_logout, name="logout"),
    path("registration/", Registration.as_view(), name="registration"),
    path("clothes/", AllClothes.as_view(), name="clothes"),
    path("clothes/<slug:clothes_slug>/", specificClothing.as_view(), name="specificClothing"),
    path("brands/", Brands.as_view(), name="brands"),
    path("brands/<slug:brand_slug>/", ItemsByBrand.as_view(), name="brandItems")
]
