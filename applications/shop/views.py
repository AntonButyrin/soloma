from django import http
from django.contrib import messages
from django.views import generic

from ..menu import models as delivery_models
from . import forms, models, telegram


class AddToCartView(generic.View):

    def get(self, *args, **kwargs):
        ct_model = kwargs.get('ct_model')
        product = delivery_models.Product.published.filter(uuid=ct_model).first()
        get_cart, _ = models.Cart.objects.get_or_create(uuid=self.request.session.session_key)
        if get_cart:
            get_cart.add(product)

        return http.HttpResponseRedirect('/#fh5co-menus')


class DeleteFromCartView(generic.View):

    def get(self, *args, **kwargs):
        ct_model = kwargs.get('ct_model')
        product = delivery_models.Product.published.filter(uuid=ct_model).first()
        get_cart, _ = models.Cart.objects.get_or_create(uuid=self.request.session.session_key)
        if get_cart:
            get_cart.remove(product)
        return http.HttpResponseRedirect('/#fh5co-cart')


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm

    def get(self, *args, **kwargs):
        return http.HttpResponseBadRequest()

    def form_invalid(self, form):
        return http.HttpResponseBadRequest()

    def form_valid(self, form):
        order = form.save()
        cart = models.Cart.objects.filter(uuid=self.request.session.session_key).first()
        for cart_item in cart.items.all():
            models.OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=1,
            )
        order.uuid = cart.uuid
        order.amount = cart.amount()
        order.save()
        cart.delete()
        messages.success(
            self.request,
            'Ваш заказ оформлен. Мы скоро Вам позвоним для подтверждения заказа.',
        )
        telegram.send_telegram(order)
        return http.HttpResponseRedirect('/#fh5co-cart')
