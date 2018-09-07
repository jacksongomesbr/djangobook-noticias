from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

# Create your views here.
from .models import Noticia, Tag


class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'


class NoticiasResumoView(View):
    template_name = 'app_noticias/resumo.html'

    def get(self, request, *args, **kwargs):
        total = Noticia.objects.count()
        return render(request, self.template_name, {'total': total})


def noticias_resumo(request):
    total = Noticia.objects.count()
    html = """
    <html>
    <body>
    <h1>Resumo</h1>
    <p>A quantiade total de notícias é {}.</p>
    </body>
    </html>
    """.format(total)
    return HttpResponse(html)


def noticias_resumo_template(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total': total})


def noticia_detalhes(request, noticia_id):
    try:
        noticia = Noticia.objects.get(pk=noticia_id)
    except Noticia.DoesNotExist:
        raise Http404('Notícia não encontrada')
    return render(request, 'app_noticias/detalhes.html', {'noticia': noticia})


def noticias_da_tag(request, tag_slug):
    try:
        tag = Tag.objects.get(slug=tag_slug)
        noticias = Noticia.objects.filter(tags__in=[tag])
    except Tag.DoesNotExist:
        raise Http404('Tag não encontrada')
    return render(request, 'app_noticias/noticias_da_tag.html', {'tag': tag, 'noticias': noticias})
