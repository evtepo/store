from django.contrib import admin
from .models import Brand, TypeOfClothing, Clothes


class MixinAdmin(admin.ModelAdmin):
    list_display = ("name", "desc",)
    search_fields = ("name",)
    prepopulated_fields = {"slug" : ("name",),}

    class Meta():
        abstract = True
        

class BrandAdmin(MixinAdmin):
    ...


class TypeOfClothingAdmin(MixinAdmin):
    ...


class ClothesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "desc",
        "types",
        "gender",
        "season",
        "fabric",
        "color",
        "publication_date",
    )
    search_fields = (
        "name",
        "gender",
        "season",
        "color",
    )
    list_filter = (
        "season",
        "gender",
        "types",
        "publication_date",
    )
    prepopulated_fields = {"slug" : ("name",),}


admin.site.register(Brand, BrandAdmin)
admin.site.register(TypeOfClothing, TypeOfClothingAdmin)
admin.site.register(Clothes, ClothesAdmin)
