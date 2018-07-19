from rest_framework import serializers
from ewebsite.models import Highlight, Service, Text_modal, Portfolio, Team, Posting

class HighlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Highlight
		fields = ('pk', 'title', 'description')

class ServiceSerializer(serializers.ModelSerializer):
	text_modals = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Service
		fields = ('pk', 'name', 'examples', 'description', 'text_modals')

class TextModalSerializer(serializers.ModelSerializer):
	service_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = Text_modal
		fields = ('pk', 'service_id', 'modal', 'text')

class PortfolioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Portfolio
		fields = ('pk', 'name', 'examples', 'video_url', 'description')

class TeamSerializer(serializers.ModelSerializer):
	postings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Team
		fields = ('pk', 'name', 'role_type', 'role', 'pos_role', 'about', 'linkedin', 'github', 'postings')

class PostingSerializer(serializers.ModelSerializer):
	author_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = Posting
		fields = ('pk', 'author_id', 'title', 'category', 'publication_date', 'text')