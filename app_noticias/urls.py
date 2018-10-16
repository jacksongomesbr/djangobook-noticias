from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('noticias/<int:pk>/', views.NoticiaDetalhesView.as_view(), name='detalhes'),
    path('noticias/resumo/', views.NoticiasResumoView.as_view(), name='resumo'),
    path('tags/<slug:slug>/', views.TagDetalhesView.as_view(), name='noticias_da_tag'),
    path('contato/', views.ContatoView.as_view(), name='contato'),
    path('contato/sucesso/', views.ContatoSucessoView.as_view(), name='contato_sucesso'),
    path('autores/<int:id>/', views.autor_detalhes, name='autor_detalhes'),
    path('categorias/<slug>/', views.categoria_detalhes, name='categoria_detalhes'),
]
