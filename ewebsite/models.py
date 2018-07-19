from django.db import models
#from stdimage.models import StdImageField
#from stdimage.utils import UploadToUUID
from django.urls import reverse

# Create your models here.

class Highlight(models.Model):
	title = models.CharField('Título', max_length=50)
	description = models.CharField('Descrição', max_length=50)
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='destaques/'), variations={'normal': (1900, 550, True)})

	def __str__(self):
		return self.title

# Services
class Service(models.Model):
	name = models.CharField(max_length=20)
	examples = models.CharField(max_length=100)
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='servicos/'), variations={'normal': (1900, 550, True)})
	description = models.TextField()

	def __str__(self):
		return self.name

class Text_modal(models.Model):
	service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
	modal = models.CharField(max_length=20)
	text = models.TextField()

	def __str__(self):
		return self.service.name

class Img_text(models.Model):
	text_modal = models.ForeignKey(Text_modal, on_delete=models.DO_NOTHING)
	#img = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='servicos/text-img'), variations={'normal': (1900, 550, True)})

	def __str__(self):
		return self.text_modal.service.name

#Portfolio
class Portfolio(models.Model):
	name = models.CharField(max_length=20)
	examples = models.CharField(max_length=100)
	video_url = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.name

# Team
class Team(models.Model):
	TYPE_ROLE_CHOICE = (
		('Docente', 'Docente'),
		('Discente', 'Discente')
	)

	ROLE_CHOICE = (
		('Coordenador', 'Coordenador'),
		('Diretor Presidente', 'Diretor Presidente'),
		('Diretor Vice-Presidente', 'Diretor Vice-Presidente'),
		('Diretor de Projetos', 'Diretor de Projetos'),
		('Gerente de Projetos', 'Gerente de Projetos'),
		('Diretor de Negócios', 'Diretor de Negócios'),
		('Gerente de Marketing', 'Gerente de Marketing'),
		('Diretor de Processos Internos', 'Diretor de Processos Internos'),
		('Gerente de Produtos Internos', 'Gerente de Produtos Internos'),
		('Membro', 'Membro'),
	)

	POS_ROLE_CHOICE = (
		(1, 'Coordenador'),
		(2, 'Diretor Presidente'),
		(3, 'Diretor Vice-Presidente'),
		(4, 'Diretor de Projetos'),
		(5, 'Gerente de Projetos'),
		(6, 'Diretor de Negócios'),
		(7, 'Gerente de Marketing'),
		(8, 'Diretor de Processos Internos'),
		(9, 'Gerente de Processos Internos'),
		(10, 'Membro'),
	)

	name = models.CharField(max_length=20)
	role_type = models.CharField(max_length=20, choices=TYPE_ROLE_CHOICE)
	role = models.CharField(max_length=20, choices=ROLE_CHOICE)
	pos_role = models.IntegerField(choices=POS_ROLE_CHOICE)
	about = models.TextField()
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='equipe/aluno'), variations={'normal': (1900, 550, True)})
	linkedin = models.CharField(max_length=100)
	github = models.CharField(max_length=100)

	def __str__(self):
		return self.name

#Postagens do blog
class Posting(models.Model):
	title = models.CharField('Título', max_length=100)
	category = models.CharField('Categoria', max_length=50)
	author = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
	publication_date = models.DateTimeField(blank=True, null=True)
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='postagens/'), variations={'normal': (1900, 550, True)})
	text = models.TextField()

	def __str__(self):
		return self.title

	# retorna um atributo do objeto para url, que relaciona com a view blog_post
	def get_absolute_url(self):
		return reverse('blog_post', args=[str(self.title)])
