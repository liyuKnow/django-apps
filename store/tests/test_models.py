from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product

# Create your tests here.


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='Fantasy', slug='fantasy')

    # def test_category_model_entry(self):
    #     """
    #     Test Category model data insertion/types/field attributes
    #     """
    #     data = self.data1
    #     self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'Fantasy')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Fantasy', slug='fantasy')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1,
                                            title='Harry Potter And The Sorcerers Stone',
                                            created_by_id=1,
                                            slug='harry-potter-and-the-sorcerers-stone',
                                            price=12.5,
                                            image='review_harry-potter-series.jpg'
                                            )

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Harry Potter And The Sorcerers Stone')
