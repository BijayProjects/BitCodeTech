from django.contrib import admin
from .models import Email_Soon
# Register your models here.

@admin.register(Email_Soon)
class EmailAdmin(admin.ModelAdmin):
    list_display=['id','eMail']