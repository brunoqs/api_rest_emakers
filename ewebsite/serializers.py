from rest_framework import serializers
from ewebsite.models import Highlight

class HighlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Highlight
		fields = ('pk', 'title', 'description')

