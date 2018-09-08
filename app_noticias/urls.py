from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('noticias/<int:noticia_id>/', views.noticia_detalhes, name='detalhes'),
    path('noticias/resumo/', views.NoticiasResumoView.as_view(), name='resumo'),
    path('tags/<slug:tag_slug>/', views.noticias_da_tag, name='noticias_da_tag'),
]
