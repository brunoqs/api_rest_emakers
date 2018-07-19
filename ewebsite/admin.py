from django.contrib import admin
from .models import *

# Register your models here.

class DestaqueAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'descricao',)

class ServicoAdmin(admin.ModelAdmin):
	list_display = ('nome',)

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('nome',)

class EquipeAdmin(admin.ModelAdmin):
	list_display = ('nome', 'tipo_cargo', 'cargo')

class PostagemAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'categoria', 'autor',)

admin.site.register(Destaque, DestaqueAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Texto_modal)
admin.site.register(Img_texto)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Postagem, PostagemAdmin)
