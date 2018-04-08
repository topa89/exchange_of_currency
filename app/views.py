from django.shortcuts import render
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings

from .models import LimitVal
from user.forms import LoginForm

def get_reserve_valute(title):
    return LimitVal.objects.get(name=title).reserve

def index(request):
    # проверка
    cache.set('BTC-RUB', 340444)
    
    

    kurs_val = {'BTC_RUB': cache.get('BTC-RUB'), 'ETH_RUB': cache.get('ETH-RUB')}
    limit = {
        'BTC': get_reserve_valute('Bitcoin'),
        'SBERBANK': int(get_reserve_valute('Сбербанк')),
        'ETC': get_reserve_valute('Ethereum'),
        'QIWI': get_reserve_valute('QIWI'),
        'form': LoginForm(),
    }

    return render(request, 'app/index.html', {'limit': limit, 'kurs_val': kurs_val})





