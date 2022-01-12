from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest, request, response
from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from store.models import Category, Product
from store.views import all_products


@skip("Decorated with reason to skip this test.")
class TestSkip (TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='Fantasy', slug='fantasy')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1,
                                            title='Harry Potter And The Sorcerers Stone',
                                            created_by_id=1,
                                            slug='harry-potter-and-the-sorcerers-stone',
                                            price=12.5,
                                            image='review_harry-potter-series.jpg'
                                            )

    def test_homepage_url(self):
        """
        Test homepage respose status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts.
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test product response status
        """
        response = self.c.get(reverse('store:product_detail', args=[
                              'harry-potter-and-the-sorcerers-stone']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test category response status
        """
        response = self.c.get(reverse('store:category_list', args=[
                              'fantasy']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
        # print(html)

    def test_view_function(self):
        request = self.factory.get(
            '/item/harry-potter-and-the-sorcerers-stone')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
