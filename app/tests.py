from django.test import TestCase
from django.urls import reverse

from .models import LimitVal
from .views import index, get_reserve_valute
# Create your tests here.
class TestApp(TestCase):
    # models
    def create_val(self,
                   index='BTC',
                   name='Bitcoin',
                   reserve=2,
                   min_val=0.03):
        return LimitVal.objects.create(
            index=index,
            name=name,
            reserve=reserve,
            min_val=min_val)
    
    def test_create_val(self):
        a = self.create_val()

        self.assertTrue(isinstance(a, LimitVal))
        self.assertEqual(a.__str__(), a.name)
        self.assertEqual(a.index, 'BTC')
        self.assertEqual(a.name, 'Bitcoin')
        self.assertEqual(a.reserve, 2)
        self.assertEqual(a.min_val, 0.03)

    def test_get_reserve(self):
        a = self.create_val()

        self.assertEqual(LimitVal.objects.get(name='Bitcoin').reserve, get_reserve_valute('Bitcoin'))

