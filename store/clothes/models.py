from django.db import models
from django.urls import reverse


class Mixin(models.Model):
    """
    Mixin class for models
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Name"
    )
    desc = models.TextField(
        verbose_name="Description"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="img/%Y/%m/%d/",
        verbose_name="Image"
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True


class Brand(Mixin):
    """
    Class for a clothing brand
    """
    def get_absolute_url(self):
        return reverse("type", kwargs={"brand_slug": self.slug})
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class TypeOfClothing(Mixin):
    """
    Class for clothing type
    """
    brands = models.ManyToManyField("Brand")

    def get_absolute_url(self):
        return reverse("type", kwargs={"type_slug": self.slug})
    
    class Meta:
        verbose_name = "Type of clothes"
        verbose_name_plural = "Types of clothing"


class Clothes(Mixin):
    """
    Class for clothes
    """
    types = models.ForeignKey(
        "TypeOfClothing",
        on_delete=models.PROTECT
    )
    gender = models.CharField(
        max_length=6
    )
    season = models.CharField(
        max_length=6,
        verbose_name="Season"
    )
    fabric = models.CharField(
        max_length=100,
        verbose_name="Fabric type"
    )
    color = models.CharField(
        max_length=100,
        verbose_name="Color"
    )
    publication_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Publication date"
    )

    def get_absolute_url(self):
        return reverse("clothes", kwargs={"clothes_slug": self.slug})

    class Meta:
        verbose_name = "Clothes"
        verbose_name_plural = "Clothes"
