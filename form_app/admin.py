from django.contrib import admin
from form_app.models import *
# Register your models here.
class general_contact_detail_admin(admin.ModelAdmin):

    model = general_contact_detail
    list_display = ['created_at', 'first_name','last_name','telphone_number','mail_address','context']

admin.site.register(general_contact_detail, general_contact_detail_admin)


class lesson_contact_detail_admin(admin.ModelAdmin):

    model = lesson_contact_detail
    list_display = ['created_at', 'first_name','last_name','gender','experience_class','experience_date', 'telphone_number','mail_address','context']



admin.site.register(lesson_contact_detail,lesson_contact_detail_admin)

class Event_Apply_Detail_admin(admin.ModelAdmin):

    model = Event_Apply_Detail
    list_display = ['event_title', 'place','addres','start_time','tickt_info','entry_fee',]


admin.site.register(Event_Apply_Detail,Event_Apply_Detail_admin)


admin.site.register(Class_Info)