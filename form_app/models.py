from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.
class general_contact_detail(models.Model):
    created_at =  models.DateTimeField(verbose_name='日付',auto_now_add=True)
    first_name = models.CharField(verbose_name='姓', max_length=30)
    last_name = models.CharField(verbose_name='名', max_length=30)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    telphone_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
    mail_address = models.EmailField(verbose_name='メールアドレス')
    context = models.CharField(verbose_name='内容',max_length=300)
    
    class Meta:
        verbose_name =_("一般の問い合わせ一覧")
        verbose_name_plural = _("一般の問い合わせ一覧")


class lesson_contact_detail(models.Model):
    created_at =  models.DateTimeField(verbose_name='日付',auto_now_add=True)
    first_name = models.CharField(verbose_name='姓', max_length=30)
    last_name = models.CharField(verbose_name='名', max_length=30)

    Gender_CHOICE = (
        ('Man','男'),
        ('Women','女'),
        ('Not specified','指定しない')
    )

    gender = models.CharField(max_length=20,choices=Gender_CHOICE,verbose_name='性別')

    Class_CHOICE = (
        ('キッズクラス','キッズクラス'),
        ('OPENクラス','OPENクラス'),
        ('初級クラス','初級クラス')
    )
    experience_class = models.CharField(max_length=20,choices=Class_CHOICE,verbose_name='体験希望クラス')

    experience_date =models.DateField(verbose_name='希望体験日')

    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    telphone_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
    mail_address = models.EmailField(verbose_name='メールアドレス')
    context = models.CharField(verbose_name='備考',max_length=300)
    
    class Meta:
        verbose_name =_("レッスンの問い合わせ一覧")
        verbose_name_plural = _("レッスンの問い合わせ一覧")


class Event_Apply_Detail(models.Model):
    event_title = models.CharField(max_length=30,verbose_name ="イベント名",unique=True)
    place = models.CharField(max_length=30,verbose_name ="会場")
    addres = models.CharField(max_length=30,verbose_name ="住所")
    start_time = models.IntegerField(verbose_name ="開演")
    tickt_info = models.IntegerField(verbose_name ="チケット")
    entry_fee = models.IntegerField(verbose_name ="参加費")

    

    date_time = models.DateField(verbose_name ="日時")
    class Meta:
        verbose_name ="イベント申し込み"
        verbose_name_plural = _("イベント申し込み")

    def __str__(self):
        return self.event_title

class Class_Info(models.Model):
    class_name = models.CharField(max_length=30,verbose_name ="クラス名")
    weekday = models.CharField(max_length=3,verbose_name ="曜日")
    start_time = models.CharField(max_length=30,verbose_name ="時間")
    genre = models.CharField(max_length=30,verbose_name ="ジャンル")
    inst = models.CharField(max_length=30,verbose_name ="インストラクター")
    playce = models.CharField(max_length=30,verbose_name ="場所")

    class Meta:
        verbose_name ="クラス情報"
        verbose_name_plural = _("クラス情報")

    def __str__(self):
        return self.class_name