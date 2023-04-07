from django.contrib import admin
from django import forms
# Register your models here.
from movie_app.models import *

class EventlistCreationForm(forms.ModelForm):
    event_title = forms.CharField(max_length=30,label="イベント名",)
    max_chapter = forms.IntegerField(label="総チャプター数",)
    event_img_src = forms.CharField(max_length=200,label="URL",)
    event_day = forms.DateField(label="イベント日",)







    def save(self, commit=True):
    # Save the provided password in hashed format
        data = super().save(commit=False)
        if commit:
            data.save()
        return data

class EventlistChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    class Meta:
        model = Eventlist
        fields = ('event_title', 'max_chapter','event_img_src','event_day',)





class EventTitleFor(admin.ModelAdmin):
    # The forms to add and change user instances
    form = EventlistChangeForm
    add_form = EventlistCreationForm
    model = Eventlist

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['event_title', 'max_chapter','event_day']
    # list_filter = ('is_admin',)
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     #('Personal info', {'fields': ('first_name','last_name',)}),
    #     ('Permissions', {'fields': ('is_admin',)}),
    # )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name','last_name' , 'password1', 'password2'),
    #     }),
    # )
    # search_fields = ('email',)
    # ordering = ('email',)
    # filter_horizontal = ()


class Movie_detile_admin(admin.ModelAdmin):
    # The forms to add and change user instances
    model = Movie_detile
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['event_title', 'video_title','number']

admin.site.register(Eventlist,EventTitleFor)
admin.site.register(Movie_detile,Movie_detile_admin)

