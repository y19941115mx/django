from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# from django.conf import settings
# from django.shortcuts import redirect



from .forms import LoginForm, RegisterForm
from .models import UserProfile, RoomType, Order

import re
# Create your views here.


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        rooms = RoomType.objects.all()
        for room in rooms:
            room.image = "/static/images/{}.jpg".format(room.img)
        return render(request, 'index.html', {'rooms': rooms})




class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            pass_word = login_form.cleaned_data['password']
            if not UserProfile.objects.filter(username=user_name):
                return render(request, 'login.html', {'msg': '用户不存在', 'login_form': login_form})
            user = authenticate(username=user_name, password=pass_word)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '密码错误', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form, 'msg': '用户名或密码格式不正确'})


class RegisterView(View):
    def post(self, request):
        req_form = RegisterForm(request.POST)
        if req_form.is_valid():
            user_name = req_form.cleaned_data['username']
            pass_word = req_form.cleaned_data['password']
            name = req_form.cleaned_data['name']
            phone = req_form.cleaned_data['phone']
            if UserProfile.objects.filter(username=user_name):
                return HttpResponse('{"status":"fail", "msg":"用户已经存在"}', content_type='application/json')
            #创建用户
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.name = name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = True
            user_profile.phone = phone
            user_profile.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"数据格式出错"}', content_type='application/json')


class OrderView(View):
    def get(self, request):
        stype = request.GET.get('type', "")
        stype = int(stype)
        room = RoomType.objects.get(type=stype)
        room.image = room.image = "/static/images/{}.jpg".format(room.img)
        #选择入住时间进入
        if request.GET.get("flag", "") != "":
            begin_time = request.GET.get("begin_time", "")
            end_time = request.GET.get("end_time", "")
            if begin_time != "" and end_time != "":
                return render(request, 'details.html', {"room":room, "flag": "0", "begin_time": self.transform_time(begin_time),
                                                        "end_time": self.transform_time(end_time)})
        #点击房型入住
        else:
            if not stype == "":
                return render(request, 'details.html', {"room": room, "flag": "1"})

    def post(self, request):
        # 提交订单
        # order =Order()
        if request.POST.get("begin_time", "") == "":
            begin_y = request.POST.get("begin_year")
            begin_m = request.POST.get("begin_month")
            begin_d = request.POST.get("begin_day")
            begin_time = datetime(int(begin_y), int(begin_m), int(begin_d))
            end_y = request.POST.get("end_year")
            end_m = request.POST.get("end_month")
            end_d = request.POST.get("end_day")
            end_time = datetime(int(end_y), int(end_m), int(end_d))
        else:
            begin_time = datetime.strptime(request.POST.get("begin_time", ""), '%Y-%m-%d')
            end_time = datetime.strptime(request.POST.get("end_time", ""), '%Y-%m-%d')
        if begin_time >= end_time:
            return HttpResponse('{"status":"fail", "msg":"日期格式不正确"}', content_type='application/json')
        stype = int(request.POST.get("type"))
        room = RoomType.objects.get(type=stype)
        sorder = Order.objects.filter(type=room) #订阅该房型的订单
        #筛选符合条件的订单
        order_num1 = sorder.filter(begin_time__lte=begin_time, end_time__gte=end_time)

        order_num2 = sorder.filter(begin_time__gt=begin_time)
        order_num3 = sorder.filter(begin_time__lt=begin_time, end_time__lt=end_time)

        room_num = 0 # 占据的房间数量
        if order_num1:
            for order in order_num1:
                room_num += order.count
        if order_num2:
            for order in order_num2:
                room_num += order.count
        if order_num3:
            for order in order_num3:
                room_num += order.count
            # 检查库存
        stock = room.count - room_num
        if stock <= 0:
            return HttpResponse('{"status":"fail", "msg":"库存不足"}', content_type='application/json')
        # 保存订单
        count = int(request.POST.get("count"))
        dic = {'type': room, 'count': count, "customer": request.POST.get("customer"),
               'phone': request.POST.get("phone"), "begin_time":begin_time, "end_time": end_time,
               "sum_price": count * room.price}
        Order.objects.create(**dic)
        return HttpResponse('{"status":"success"}', content_type='application/json')


    def transform_time(self, time_str):
        return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', time_str)


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

