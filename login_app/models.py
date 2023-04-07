from email.mime import image

# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.core import validators

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=255,
        unique=True,null=True
    )
    first_name = models.CharField(max_length=10,verbose_name ="姓")
    last_name = models.CharField(max_length=10,verbose_name ="名")
    first_kana = models.CharField(max_length=10,verbose_name ="セイ")
    last_kana = models.CharField(max_length=10,verbose_name ="メイ")
    number_of_student = models.IntegerField(verbose_name ="生徒数",null=True)
    is_movie_subscription = models.BooleanField(default=False,verbose_name ="動画登録")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name','last_name']
    class Meta:
        verbose_name = _("親ユーザー一覧")
        verbose_name_plural = _("親ユーザー一覧")


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




class UserStudent(AbstractBaseUser):
    department = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10,verbose_name ="姓")
    last_name = models.CharField(max_length=10,verbose_name ="名")
    first_kana = models.CharField(max_length=10,verbose_name ="セイ")
    last_kana = models.CharField(max_length=10,verbose_name ="メイ")
    email = models.EmailField(_("email address"), blank=True)
    is_active = models.BooleanField(default=True)
    #objects = MyUserManager()


    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    


    class Meta:
        verbose_name = _("生徒一覧")
        verbose_name_plural = _("生徒一覧")
        #abstract = True

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


# class PerformanceList(models.Model):

#     Performancelist = (
#         ('選択してください','選択してください'),
#         ('YOASOBI', 'YOASOBI'),
#         ('座頭市', '座頭市'),
#         ('voice&diggy', 'voice&diggy'),
#         ('MEE TOO', 'MEE TOO'),
#     )
#     # Fields
#     name = models.CharField(max_length=32)
#     select_Performance = models.CharField(max_length=1,
#                             choices=Performancelist,
#                             verbose_name='作品名',
#                             )
#     entry_fee = models.IntegerField(verbose_name="参加費")
#     rehearsal_price = models.IntegerField(verbose_name="リハーサル代")

    
#     class Meta:
#         verbose_name ="イベント申し込みフォーム"
#         verbose_name_plural = _("イベント申し込みフォーム")

#     def __str__(self):
#         return self.event_title

class PerformanceList(models.Model):

    # Fields
    performance_name = models.CharField(max_length=32,
                            verbose_name='作品名',
                            )
    
    rehearsal_time = models.IntegerField(verbose_name="リハーサル時間",
                                         validators=[validators.MinValueValidator(0)]
                                         )

    
    class Meta:
        verbose_name ="作品申し込み詳細"
        verbose_name_plural = _("作品申し込み詳細")

    def __str__(self):
        return self.event_name