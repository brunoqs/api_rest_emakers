from django.contrib import admin
from .models import *

# Register your models here.

class HighlightAdmin(admin.ModelAdmin):
	list_display = ('title', 'description',)

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name',)

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('name',)

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'role_type', 'role')

class PostingAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'author',)

admin.site.register(Highlight, HighlightAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Text_modal)
admin.site.register(Img_text)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Posting, PostingAdmin)
