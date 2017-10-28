from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='用户手机号')
    name = models.CharField(max_length=10, verbose_name='中文名')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class RoomType(models.Model):
    count = models.IntegerField(default=0, verbose_name='房型库存')
    type = models.IntegerField(default=3, verbose_name='房型类别', choices=((0, '豪华大床房'), (1, '普通大床房'), (2, '高级标准间'),
                                                                        (3, '普通标准间'), (4, '商务套房'), (5, '行政豪华套房'),
                                                                        (6, '家庭房')))
    desc = models.TextField(verbose_name='房型描述')
    price = models.IntegerField(default=0, verbose_name='价格')
    discount = models.IntegerField(default=0, verbose_name='折扣')
    img = models.IntegerField(default=0, verbose_name='图片')

    class Meta:
        verbose_name = '房型信息'
        verbose_name_plural = verbose_name

    def get_type_name(self):
        if self.type == 0:
            return u"豪华大床房"
        elif self.type == 1:
            return u"普通大床房"
        elif self.type == 2:
            return u"高级标准间"
        elif self.type == 3:
            return u"普通标准间"
        elif self.type == 4:
            return u"商务套房"
        elif self.type == 5:
            return u"行政豪华套房"
        elif self.type == 6:
            return u"家庭房"
        else:
            return u"请选择房型"

    def __str__(self):
        return self.get_type_name()


class Order(models.Model):
    number = models.AutoField(primary_key=True, verbose_name='订单号',)
    order_date = models.DateField(auto_now_add=True, verbose_name='订购日期')
    type = models.ForeignKey(RoomType, verbose_name='房型')
    customer = models.CharField(max_length=20, verbose_name='入住人姓名')
    phone = models.CharField(max_length=50, verbose_name='电话')
    sum_price = models.IntegerField(default=0, verbose_name='订购总价')
    count = models.IntegerField(default=1, verbose_name='订购数量')
    begin_time = models.DateField(verbose_name='入住日期')
    end_time = models.DateField(verbose_name='离店日期')

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.number)









