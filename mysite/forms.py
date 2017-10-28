# -*- coding:utf-8 -*-
# __author__ = 'victor'
# __date__ = '2017/10/27 下午2:40'

# -*- coding:utf-8 -*-
from django import forms
from .models import UserProfile, Order


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=5)
    password = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
    phone = forms.CharField(required=True, min_length=5)
    name = forms.CharField(required=True, min_length=1)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['begin_time', "end_time", "sum_price", "type"]

