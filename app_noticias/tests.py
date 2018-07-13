from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Noticia


# Create your tests here.
class NoticiaModelTest(TestCase):
    def setUp(self):
        Noticia.objects.create(titulo='Noticia X', conteudo='Conteudo')

    def test_deve_encontrar_noticia_x(self):
        noticia = Noticia.objects.get(titulo='Noticia X')
        self.assertEqual(noticia.titulo, 'Noticia X')

    def test_deve_encontrar_noticia_com_id_1(self):
        noticia = Noticia.objects.get(id=1)
        self.assertEqual(noticia.id, 1)

    def test_deve_gerar_excecao_para_encontrar_noticia_com_id_2(self):
        with self.assertRaisesMessage(Noticia.DoesNotExist, 'Noticia matching query does not exist'):
            noticia = Noticia.objects.get(id=2)


class HomePageViewTests(TestCase):
    def setUp(self):
        Noticia.objects.create(titulo='Noticia X', conteudo='Conteudo')

    def test_home_status_code_deve_ser_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_deve_encontrar_url_por_nome(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_deve_usar_template_correto(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_noticias/home.html')
