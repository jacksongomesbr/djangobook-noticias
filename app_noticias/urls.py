from django.urls import path

from app_noticias.views import noticia_detalhes, noticias_da_tag, noticias_resumo, noticias_resumo_template, \
    NoticiasResumoView
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('noticias/<int:noticia_id>/', noticia_detalhes, name='detalhes'),
    path('noticias/resumo/', NoticiasResumoView.as_view(), name='resumo'),
    path('tags/<slug:tag_slug>/', noticias_da_tag, name='noticias_da_tag'),
]
