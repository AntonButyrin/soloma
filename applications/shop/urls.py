from django.urls import path

from . import views

urlpatterns = [
    path(
        'quick_buy/<str:ct_model>/',
        views.AddToCartView.as_view(),
        name='quick_buy',
    ),
    path(
        'product_delete/<str:ct_model>/',
        views.DeleteFromCartView.as_view(),
        name='product_delete',
    ),
    path(
        'ordering/',
        views.OrderCreateView.as_view(),
        name='order_create',
    ),
]
