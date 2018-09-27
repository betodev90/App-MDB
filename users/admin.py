from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreateForm, CustomUserEditForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserEditForm
    list_display = ['email', 'username', 'age']
    list_editable = ['age',]
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)