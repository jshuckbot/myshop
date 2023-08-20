from django import forms

from orderapp import models as orderapp_models


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = orderapp_models.Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]
