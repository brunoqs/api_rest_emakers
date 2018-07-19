from django.db import models
#from stdimage.models import StdImageField
#from stdimage.utils import UploadToUUID
from django.urls import reverse

# Create your models here.

class Destaque(models.Model):
	titulo = models.CharField('Título', max_length=50)
	descricao = models.CharField('Descrição', max_length=50)
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='destaques/'), variations={'normal': (1900, 550, True)})

	def __str__(self):
		return self.titulo

# Servicos
class Servico(models.Model):
	nome = models.CharField(max_length=20)
	exemplos = models.CharField(max_length=100)
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='servicos/'), variations={'normal': (1900, 550, True)})
	descricao = models.TextField()

	def __str__(self):
		return self.nome

class Texto_modal(models.Model):
	servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)
	modal = models.CharField(max_length=20)
	texto = models.TextField()

	def __str__(self):
		return self.servico.nome

class Img_texto(models.Model):
	texto_modal = models.ForeignKey(Texto_modal, on_delete=models.DO_NOTHING)
	#img = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='servicos/texto-img'), variations={'normal': (1900, 550, True)})

	def __str__(self):
		return self.texto_modal.servico.nome

#Portfolio
class Portfolio(models.Model):
	nome = models.CharField(max_length=20)
	exemplos = models.CharField(max_length=100)
	video_url = models.CharField(max_length=100)
	descricao = models.TextField()

	def __str__(self):
		return self.nome

# Equipe
class Equipe(models.Model):
	TIPO_CARGO_CHOICE = (
		('Docente', 'Docente'),
		('Discente', 'Discente')
	)

	CARGO_CHOICE = (
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

	POS_CARGO_CHOICE = (
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

	nome = models.CharField(max_length=20)
	tipo_cargo = models.CharField(max_length=20, choices=TIPO_CARGO_CHOICE)
	cargo = models.CharField(max_length=20, choices=CARGO_CHOICE)
	pos_cargo = models.IntegerField(choices=POS_CARGO_CHOICE)
	sobre = models.TextField()
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='equipe/aluno'), variations={'normal': (1900, 550, True)})
	linkedin = models.CharField(max_length=100)
	github = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

#Postagens do blog
class Postagem(models.Model):
	titulo = models.CharField('Título', max_length=100)
	categoria = models.CharField('Categoria', max_length=50)
	autor = models.ForeignKey(Equipe, on_delete=models.DO_NOTHING)
	data_publicacao = models.DateTimeField(blank=True, null=True)
	#imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='postagens/'), variations={'normal': (1900, 550, True)})
	texto = models.TextField()

	def __str__(self):
		return self.titulo

	# retorna um atributo do objeto para url, que relaciona com a view blog_post
	def get_absolute_url(self):
		return reverse('blog_post', args=[str(self.titulo)])
