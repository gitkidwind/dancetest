from django import forms
from django.db import models
from login_app.models import UserStudent, MyUser


class PerformanceList(models.TextChoices):
    nothing = '選択してください','選択してください'
    YOASOBI = 'YOASOBI', 'YOASOBI'
    zatouichi = '座頭市', '座頭市'
    voice_and_diggy = 'voice&diggy', 'voice&diggy'
    MEE_TOO = 'MEE TOO', 'MEE TOO'


class PerformanceListForm(forms.Form):
    food = forms.fields.ChoiceField(
        choices=PerformanceList.choices,
        required=True,
        label='作品名',
        widget=forms.widgets.Select,
    )
    entry_fee = forms.IntegerField

class UserStudent_Form(forms.Form):
    model = UserStudent
    first_name = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'姓', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    last_name = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'名', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    first_kana = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'姓', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    last_kana = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'名', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    mail_address = forms.EmailField(label='メールアドレス',
                                    widget=forms.TextInput(
                                        attrs={
                                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }
                                    ),

                                     help_text='※ご確認の上、正しく入力してください。')


class MyUser_Form(forms.Form):
    model = MyUser
    first_name = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'姓', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    last_name = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'名', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    first_kana = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'姓', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    last_kana = forms.CharField(label='名前', max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder':'名', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )
    email = forms.EmailField(label='メールアドレス',
                                    widget=forms.TextInput(
                                        attrs={
                                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }
                                    ),

                                     help_text='※ご確認の上、正しく入力してください。')
    number_of_student = forms.IntegerField(label='生徒数',
            widget=forms.TextInput(
                attrs={'placeholder':'生徒数', 
                        'class':'w-1/2 rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                        })
            )



