from django.shortcuts import render

from .models import LimitVal


# from django.conf import settings


# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
# from .tasks import periodic_task

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_reserve_valute(title):
    return LimitVal.objects.get(name=title).reserve


# @cache_page(CACHE_TTL)
def index(request):
    kurs_val = {'BTC_RUB': 556304}
    limit = {
        'BTC': get_reserve_valute('Bitcoin'),
        'SBERBANK': get_reserve_valute('Сбербанк'),
        'ETC': get_reserve_valute('Ethereum'),
        'QIWI': get_reserve_valute('QIWI'),
    }

    return render(request, 'app/index.html', {'limit': limit, 'kurs_val': kurs_val})





