from django.test import TestCase

from .models import Brand, TypeOfClothing, Clothes

# Create your tests here.
class BrandTestCase(TestCase):
    def setUp(self) -> None:
        Brand.objects.create(
            name="Brand1",
            desc="Description of Brand1",
            slug="brand1",
            image="None"
        )
        Brand.objects.create(
            name="Brand2",
            desc="Description of Brand2",
            slug="brand2",
            image="None"
        )
        Brand.objects.create(
            name="Brand3",
            desc="Description of brand3",
            slug="not-brand3",
            image="None"
        )

    def test_brands_name_eq_slug(self):
        brand1 = Brand.objects.get(name="Brand1")
        brand2 = Brand.objects.get(name="Brand2")
        brand3 = Brand.objects.get(name="Brand3")

        brands = (brand1, brand2)

        for brand in brands:
            self.assertEqual(brand.name.lower(), " ".join(brand.slug.split("-")))

        self.assertNotEqual(brand3.name.lower(), brand3.slug)
        self.assertEqual(brand3.slug, "not-brand3")


class ClothesTestCase(TestCase):
    def setUp(self) -> None:
        brnd = Brand.objects.create(
            name="Brand1",
            desc="Description of Brand1",
            slug="brand1",
            image="None"
        )
        tp = TypeOfClothing.objects.create(
            name="Type1",
            desc="Description of Type1",
            slug="type1",
            image="None"
        )
        Clothes.objects.create(
            name="Clothes1",
            desc="Description of the Clothes1",
            slug="clothes1",
            image="None",
            brand=brnd,
            type=tp,
            fabric="Cotton",
            color="Black",
            price=190.00,
        )

    def test_clothes(self):
        clothes = Clothes.objects.get(name="Clothes1")

        self.assertEqual(clothes.name.lower(), clothes.slug)
        self.assertEqual(clothes.brand.name, "Brand1")
        self.assertEqual(clothes.type.name, "Type1")
        self.assertEqual(float(clothes.price), 190.00)
        self.assertEqual(clothes.color, "Black")
