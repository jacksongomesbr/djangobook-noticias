from django.db import models

# Create your models here.
class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    titulo = models.CharField('título', max_length=128)
    conteudo = models.TextField('conteúdo')

    def __str__(self):
        return self.titulo

