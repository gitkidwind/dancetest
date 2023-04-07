from django import forms
from sqlalchemy import null
from django.utils import timezone
from form_app.models import lesson_contact_detail,general_contact_detail,Event_Apply_Detail

class general_contact(forms.Form):
    model = general_contact_detail
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
    telphone_number = forms.CharField(label='電話番号',
                                    widget=forms.TextInput(
                                    attrs={
                                    'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                    }),
                                    max_length=15,
                                    help_text='※半角数字で入力してください'
                                    )
    mail_address = forms.EmailField(label='メールアドレス',
                                    widget=forms.TextInput(
                                        attrs={
                                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }
                                    ),

                                     help_text='※ご確認の上、正しく入力してください。')
    
    context = forms.CharField(label='備考',
                                max_length=300,
                                required=False,
                                widget=forms.TextInput(
                                        attrs={
                                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }
                                    ),                                    
                                )

class lesson_contact(forms.Form):
    model = lesson_contact_detail
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

    Gender_CHOICE = {
        ('Man','男'),
        ('Women','女'),
        ('Not specified','指定しない')
        }
    gender = forms.ChoiceField(
            label='性別', 
            widget=forms.Select(
            attrs={
                    'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                }), 
            choices= Gender_CHOICE,
            initial=1,
            )
    
    Class_CHOICE = {
        ('キッズクラス','キッズクラス'),
        ('OPENクラス','OPENクラス'),
        ('初級クラス','初級クラス')
        }

    experience_class = forms.ChoiceField(
                    label='希望クラス', 
                    widget=forms.Select(
                    attrs={
                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                            }), 
                    choices= Class_CHOICE,
                    initial=1)
    
    experience_date = forms.DateField(
                                        label='希望体験日',
                                        widget=forms.DateInput(
                                            attrs={"type": "date",
                                                    'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }),
                                        input_formats=['%Y-%m-%d']
                                        )
    
    telphone_number = forms.CharField(label='電話番号',
                                      widget=forms.TextInput(
                                        attrs={
                                        'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }),
                                      max_length=15,
                                      help_text='※半角数字で入力してください'
                                      )

    
    mail_address = forms.EmailField(label='メールアドレス',
                                    widget=forms.TextInput(
                                        attrs={
                                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }
                                    ),

                                     help_text='※ご確認の上、正しく入力してください。')
    
    context = forms.CharField(label='備考',
                                max_length=300,
                                required=False,
                                widget=forms.TextInput()
                                )

class event_apply_detail_Form(forms.Form):
    model = Event_Apply_Detail
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
    telphone_number = forms.CharField(label='電話番号',
                                    widget=forms.TextInput(
                                    attrs={
                                    'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                    }),
                                    max_length=15,
                                    help_text='※半角数字で入力してください'
                                    )
    mail_address = forms.EmailField(label='メールアドレス',
                                    widget=forms.TextInput(
                                        attrs={
                                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }
                                    ),

                                     help_text='※ご確認の上、正しく入力してください。')
    
    context = forms.CharField(label='備考',
                                max_length=300,
                                required=False,
                                widget=forms.TextInput(
                                        attrs={
                                            'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
                                        }
                                    ),                                    
                                )
                                	#gpl80156@os3-314-46566.vs.sakura.ne.jp
                                    #adXbh66SzA3wzU3