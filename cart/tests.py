from django.test import TestCase 
from django.contrib.auth.models import User 
from .models import Product, CartItem 
from decimal import Decimal

class CartItemTestCase(TestCase): 
    def setUp(self): 
        self.user = User.objects.create_user(username='testuser', password='testpass') 
        self.product = Product.objects.create(name='Test Product', price=10.00)

    def test_add_cart_item(self):
        cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)
        self.assertEqual(cart_item.total_price(), Decimal('20.00'))

    def test_cart_item_str(self):
        cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)
        self.assertEqual(str(cart_item), f"2 x Test Product for testuser")