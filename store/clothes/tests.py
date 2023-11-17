from django.test import TestCase

from .models import Brand, TypeOfClothing, Clothes

# Create your tests here.
class BrandTestCase(TestCase):
    def setUp(self) -> None:
        Brand.objects.create(
            name="Puma",
            desc="Description of puma",
            slug="puma",
            image="None"
        )
        Brand.objects.create(
            name="TNF",
            desc="Description of tnf",
            slug="tnf",
            image="None"
        )
        Brand.objects.create(
            name="Zara",
            desc="Description of zara",
            slug="adidas",
            image="None"
        )

    def test_brands_name_eq_slug(self):
        puma = Brand.objects.get(name="Puma")
        tnf = Brand.objects.get(name="TNF")
        zara = Brand.objects.get(name="Zara")

        brands = (puma, tnf)

        for brand in brands:
            self.assertEqual(brand.name.lower(), brand.slug)

        self.assertNotEqual(zara.name.lower(), zara.slug)
        self.assertEqual(zara.slug, "adidas")


class ClothesTestCase(TestCase):
    def setUp(self) -> None:
        brnd = Brand.objects.create(
            name="Zara",
            desc="Description of zara",
            slug="adidas",
            image="None"
        )
        tp = TypeOfClothing.objects.create(
            name="Outerwear",
            desc="Description of outerwear",
            slug="outerwear",
            image="None"
        )
        Clothes.objects.create(
            name="Jacket",
            desc="Description of the jacket",
            slug="jacket",
            image="None",
            brand=brnd,
            type=tp,
            fabric="Cotton",
            color="Black",
            price=190.00,
        )

    def test_clothes(self):
        clothes = Clothes.objects.get(name="Jacket")

        self.assertEqual(clothes.name.lower(), clothes.slug)
        self.assertEqual(clothes.brand.name, "Zara")
        self.assertEqual(clothes.type.name, "Outerwear")
        self.assertEqual(float(clothes.price), 190.00)
        self.assertEqual(clothes.color, "Black")
