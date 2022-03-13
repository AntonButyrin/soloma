from django import forms

from . import models


class OrderForm(forms.ModelForm):
    message = forms.CharField(
        label='Комментарий',
        required=False,
    )

    class Meta:
        model = models.Order
        fields = [
            'name',
            'phone',
            'address',
            'message',
        ]
