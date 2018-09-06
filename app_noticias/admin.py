from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass
