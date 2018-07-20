from rest_framework import serializers
from ewebsite.models import Highlight, Service, Text_modal, Portfolio, Team, Posting

class HighlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Highlight
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

class TextModalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text_modal
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

class PostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posting
        fields = '__all__'