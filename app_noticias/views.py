from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, FormView

# Create your views here.
from app_noticias.forms import ContatoForm
from .models import *


class HomePageView(ListView):
    model = Noticia
    context_object_name = 'noticias'
    template_name = 'app_noticias/home.html'

    def get_queryset(self):
        return Noticia.objects.exclude(data_de_publicacao=None).order_by('-data_de_publicacao')[:5]


class NoticiasResumoView(TemplateView):
    template_name = 'app_noticias/resumo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Noticia.objects.count()
        return context


class NoticiaDetalhesView(DetailView):
    model = Noticia
    template_name = 'app_noticias/detalhes.html'


class TagDetalhesView(DetailView):
    model = Tag
    template_name = 'app_noticias/noticias_da_tag.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.filter(tags__in=[self.object])
        return context


class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(
            nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')


class ContatoSucessoView(TemplateView):
    template_name = 'app_noticias/contato_sucesso.html'


def noticias_da_tag(request, tag_slug):
    try:
        tag = Tag.objects.get(slug=tag_slug)
        noticias = Noticia.objects.filter(tags__in=[tag])
    except Tag.DoesNotExist:
        raise Http404('Tag não encontrada')
    return render(request, 'app_noticias/noticias_da_tag.html', {'tag': tag, 'noticias': noticias})


def noticia_detalhes(request, id):
    try:
        n = Noticia.objects.get(pk=id)
        return render(request, 'app_noticias/detalhes.html', {'noticia': n})
    except Noticia.DoesNotExist:
        return Http404('Notícia não encontrada')


def autor_detalhes(request, id):
    try:
        pessoa = Pessoa.objects.get(pk=id)
        noticias = Noticia.objects.filter(autor=pessoa)
        return render(request, 'app_noticias/autor.html', {
            'autor': pessoa,
            'noticias': noticias
        })
    except Pessoa.DoesNotExist:
        return Http404('Este autor não foi encontrado')


def categoria_detalhes(request, slug):
    try:
        categoria = Categoria.objects.get(slug=slug)
        noticias = Noticia.objects.filter(categoria=categoria)
        porcentagem = noticias.count()/Noticia.objects.count()*100
        return render(request, 'app_noticias/categoria.html', {
            'categoria': categoria,
            'noticias': noticias,
            'porcentagem': porcentagem
        })
    except Categoria.DoesNotExist:
        return Http404('Categoria não encontrada')
