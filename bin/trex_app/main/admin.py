from django.contrib import admin
from models import *
# Register your models here.

class InfoAdm(admin.StackedInline):
    model = Main
    extra = 2

class AdminInfo(admin.ModelAdmin):
    pass

admin.site.register(Main)
