from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from ewebsite.models import Highlight, Service, Text_modal, Portfolio, Team, Posting
from ewebsite.serializers import HighlightSerializer, ServiceSerializer, TextModalSerializer, PortfolioSerializer, TeamSerializer, PostingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class HighlightViewSet(viewsets.ModelViewSet):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = (IsAuthenticatedOrReadOnly),

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly),

class TextModalViewSet(viewsets.ModelViewSet):
    queryset = Text_modal.objects.all()
    serializer_class = TextModalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly),

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (IsAuthenticatedOrReadOnly),

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly),

class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly),