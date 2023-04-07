from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Hoge(models.Model):
    mmdd = models.DateField()
    class Meta:
        verbose_name ="ほげ"
        verbose_name_plural = _("ほげ")

    def __int__(self):
        return self.mmdd


class Eventlist(models.Model):
    event_title = models.CharField(max_length=30,verbose_name ="イベント名",unique=True)
    max_chapter = models.IntegerField(verbose_name ="総チャプター数",)
    event_img_src = models.TextField(max_length=200,blank=True,verbose_name = "URL")
    event_day = models.DateField(verbose_name = "イベント日",blank=True)
    class Meta:
        verbose_name ="イベント一覧"
        verbose_name_plural = _("イベント一覧")

    def __str__(self):
        return self.event_title

class Movie_detile(models.Model):
    event_title = models.CharField(max_length=30,verbose_name ="イベント名",unique=True)

    video_title = models.CharField(max_length=30,verbose_name ="作品名")
    number = models.IntegerField(verbose_name ="チャプター番号")
    video_path = models.CharField(max_length=30,verbose_name ="ビデオパス")
    img_path = models.CharField(max_length=30,verbose_name ="イメージパス")
    class Meta:
        verbose_name ="動画一覧"
        verbose_name_plural = _("動画一覧")

    def __str__(self):
        return self.event_title