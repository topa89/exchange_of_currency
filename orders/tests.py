from django.test import TestCase

from .models import Orders
from django.urls import reverse
# Create your tests here.
class TestOrders(TestCase):
    def create_order(self,
                     email='test@mail.com',
                     card_number='1234 5678 1234 5678',
                     input_val='BTC',
                     output_val='RUB',
                     sum_from='1',
                     sum_to='2'):
        return Orders.objects.create(
                     email=email,
                     card_number=card_number,
                     input_val=input_val,
                     output_val=output_val,
                     sum_from=sum_from,
                     sum_to=sum_to)
    
    def test_create_order(self):
        a = self.create_order()

        self.assertTrue(isinstance(a, Orders))
        self.assertEqual(a.__str__(), '{}, {} -> {}'.format(a.email , a.input_val, a.output_val))
        self.assertEqual(a.email, 'test@mail.com')
        self.assertEqual(a.card_number, '1234 5678 1234 5678')
        self.assertEqual(a.input_val, 'BTC')
        self.assertEqual(a.output_val, 'RUB')
        self.assertEqual(a.sum_from, '1')
        self.assertEqual(a.sum_to, '2')
    
    def test_show_all_orders(self):
        url = reverse('orders')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_open_admin(self):
        url = reverse('adminp')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)