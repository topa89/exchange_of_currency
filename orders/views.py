from django.shortcuts import render

from django.http import JsonResponse
from .models import Orders

from django.core.mail import EmailMessage


def open_admin(request):
    order = {
        'orders': Orders.objects.all(),
        }
    return render(request, 'orders/index.html', order)

def all_orders(request):
    orders = {
        'orders': Orders.objects.all()
        }
    return render(request, 'orders/tables.html', orders)

def send_order(request):
    post = request.POST
    email = post['email']
    card_number = post['card_number']
    sum_to = post['sum_to']
    input_val = post['input']
    output_val = post['output']
    sum_from = post['sum_from']

    msg = EmailMessage(
        subject=u'Обменник',
        body=u'Ваш заказ в обработке. \nНа карту ' + card_number + ' будет зачислено ' + sum_to + ' р',
        from_email='antondranicyn6@gmail.com',
        to=(email,)
    )
    msg.content_subtype = 'html'
    msg.send()

    new_order = Orders.objects.create(email=email, card_number=card_number, input_val=input_val, output_val=output_val,
    sum_from=sum_from, sum_to=sum_to)

    return_dict = dict()
    print(post)
    return JsonResponse(return_dict)

