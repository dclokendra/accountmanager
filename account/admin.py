from django.contrib import admin
from .models import Account
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# Register your models here.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password Confirmation', widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('email', 'contact_no')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password does not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False) # commit =False does not save in database password still needed to be set
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'password', 'contact_no', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'contact_no', 'is_admin','is_active')
    list_filter = ('is_admin', 'is_active')
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('personal info', {'fields': ('contact_no',)}),
        ('permissions', {'fields': ('is_admin',)}),

    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'contact_no', 'is_admin', 'is_active'),
    #     }),
    # )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields': ('email','contact_no','password1','password2','is_admin','is_active'),
        }),
    )
    filter_horizontal = []
    # ordering = ('-email',) for descending order
    ordering = ('email',)


admin.site.register(Account, UserAdmin)
