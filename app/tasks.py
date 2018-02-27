from celery.task.schedules import crontab
from celery.decorators import periodic_task
# from django.core.cache import cache
import requests
import json


def get_kurs(query):
    valuta = requests.get('https://api.cryptonator.com/api/ticker/' + query.lower(), timeout=5).json()
    return valuta['ticker']['price']


@periodic_task(run_every=(crontab(minute='*/1')), name="task_get_kurs", ignore_result=True)
def task_get_kurs():
    kurs = ('BTC-RUB', 'BTC-ETH', 'ETH-RUB')
    new_kurs = {}
    # cache.set("key", "value1", timeout=22)
    for i in kurs:
        new_kurs[i] = get_kurs(i)

    f = open('kurs.json', 'wb')
    f.write(json.dumps(new_kurs, ensure_ascii=False,
                       sort_keys=True).encode('UTF-8'))
    f.close()
