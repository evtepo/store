from django.test import TestCase

from .models import Brand, TypeOfClothing, Clothes


class Mixin(TestCase):
    def setUp(self) -> None:
        brand1 = Brand.objects.create(
            name="Brand1",
            desc="Description Brand1",
            slug="brand1",
            image="imageUrl"
        )
        type1 = TypeOfClothing.objects.create(
            name="Type1",
            desc="Description Type1",
            slug="type1",
            image="imageUrl"
        )
        Clothes.objects.create(
            name="Clothes1",
            desc="Description Clothes1",
            slug="clothes1",
            image="imageUrl",
            brand=brand1,
            type=type1,
            fabric="Cotton",
            color="Black",
            price=190.00,
        )


# Page testing
class PageTestCase(Mixin):
    def test_pages(self):
        brand1 = self.brand1
        type1 = TypeOfClothing.objects.get(name="Type1")
        clothes1 = Clothes.objects.get(name="Clothes1")
        print(brand1.name)

        self.assertEqual(self.client.get("/").status_code, 200)
        # self.assertEqual(self.client.get("/authentication/").status_code, 200)
        # self.assertEqual(self.client.get("/logout").status_code, 301)
        # self.assertEqual(self.client.get("/registration").status_code, 301)
        # self.assertEqual(self.client.get("/clothes").status_code, 200)
        # self.assertEqual(self.client.get("/clothes/<slug:clothes_slug>").status_code, 200)
        # self.assertEqual(self.client.get("/brands/").status_code, 200)
        # self.assertEqual(self.client.get(f"/brands/<slug:{brand1.slug}>/").status_code, 200)


# Model testing.
class ClothesTestCase(Mixin):
    def test_items(self):
        brand1 = Brand.objects.get(name="Brand1")
        type1 = TypeOfClothing.objects.get(name="Type1")
        clothes1 = Clothes.objects.get(name="Clothes1")

        items = (brand1, type1, clothes1)

        # Basic testing
        for item in items:
            self.assertEqual(item.name.lower(), " ".join(item.slug.split("-")))
            self.assertIn("Description ", item.desc)

        # Clothes testing
        self.assertEqual(clothes1.brand.name, "Brand1")
        self.assertEqual(clothes1.type.name, "Type1")
        self.assertEqual(clothes1.fabric, "Cotton")
        self.assertEqual(clothes1.color, "Black")
        self.assertEqual(float(clothes1.price), 190.00)
