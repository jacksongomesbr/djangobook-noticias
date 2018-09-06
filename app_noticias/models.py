from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField(
        'Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15,
                                        help_text='Número do telefone celular no formato (99) 99999-9999',
                                        null=True, blank=True,
                                        )
    telefone_fixo = models.CharField('Telefone fixo', max_length=14,
                                     help_text='Número do telefone fixo no formato (99) 9999-9999',
                                     null=True, blank=True,
                                     )
    email = models.EmailField('E-mail', null=True, blank=True)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    titulo = models.CharField('Título', max_length=128)
    conteudo = models.TextField('Conteúdo')
    data_de_publicacao = models.DateTimeField(
        'Data de publicação', blank=True, null=True)
    autor = models.ForeignKey(
        Pessoa, on_delete=models.SET_NULL, related_name='noticias', blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.titulo
