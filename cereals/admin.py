from django.contrib import admin
from .models import cereal

# Register your models here.

@admin.register(cereal)
class cerealAdmin(admin.ModelAdmin):
	list_display =('name','protein','fat','fiber','rating')
	list_filter= ('fat','protein')
	ordering =('-rating',)
