from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram


def first_page(request):
    slider_list = CmsSlider.objects.all()
    pk_1 = PriceCard.objects.get(pk=1)
    pk_2 = PriceCard.objects.get(pk=2)
    pk_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pk_1': pk_1,
                'pk_2': pk_2,
                'pk_3': pk_3,
                'price_table': price_table,
                'form': form,
    }
    return render(request, 'index.html', dict_obj)


def thanks_page(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    element = Order(order_name='name', order_phone='phone')
    element.save()
    sendTelegram(tg_name=name, tg_phone=phone)
    return render(request, 'thanks.html', {'name': name, })
