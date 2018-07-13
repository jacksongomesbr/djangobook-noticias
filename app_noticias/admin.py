from django.contrib import admin

# Register your models here.
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass
