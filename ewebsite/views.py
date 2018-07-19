from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from ewebsite.models import Highlight, Service, Text_modal, Portfolio, Team, Posting
from ewebsite.serializers import HighlightSerializer, ServiceSerializer, TextModalSerializer, PortfolioSerializer, TeamSerializer, PostingSerializer

# Create your views here.

class HighlightViewSet(viewsets.ViewSet):
	def list(self, request):
		highlights = Highlight.objects.all()
		serializer = HighlightSerializer(highlights, many=True)
		return Response(serializer.data)	

	def create(self, request):
		serializer = HighlightSerializer(data=request.data)
		if serializer.is_valid(): 
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		try:
			highlight = Highlight.objects.get(pk=pk)
		except Highlight.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = HighlightSerializer(highlight)
		return Response(serializer.data)

	def update(self, request, pk=None):
		try:
			highlight = Highlight.objects.get(pk=pk)
		except Highlight.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = HighlightSerializer(highlight, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		try:
			highlight = Highlight.objects.get(pk=pk)
		except Highlight.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		highlight.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ServiceViewSet(viewsets.ViewSet):
	def list(self, request):
		services = Service.objects.all()
		serializer = ServiceSerializer(services, many=True)
		return Response(serializer.data)	

	def create(self, request):
		serializer = ServiceSerializer(data=request.data)
		if serializer.is_valid(): 
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		try:
			service = Service.objects.get(pk=pk)
		except Service.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = ServiceSerializer(service)
		return Response(serializer.data)

	def update(self, request, pk=None):
		try:
			service = Service.objects.get(pk=pk)
		except Service.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = ServiceSerializer(service, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		try:
			service = Service.objects.get(pk=pk)
		except Service.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		service.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class TextModalViewSet(viewsets.ViewSet):
	def list(self, request):
		text_modals = Text_modal.objects.all()
		serializer = TextModalSerializer(text_modals, many=True)
		return Response(serializer.data)	

	def create(self, request):
		serializer = TextModalSerializer(data=request.data)
		if serializer.is_valid(): 
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		try:
			text_modal = Text_modal.objects.get(pk=pk)
		except Text_modal.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = TextModalSerializer(text_modal)
		return Response(serializer.data)

	def update(self, request, pk=None):
		try:
			text_modal = Text_modal.objects.get(pk=pk)
		except Text_modal.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = TextModalSerializer(text_modal, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		try:
			text_modal = Text_modal.objects.get(pk=pk)
		except Text_modal.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		text_modal.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PortfolioViewSet(viewsets.ViewSet):
	def list(self, request):
		portfolios = Portfolio.objects.all()
		serializer = PortfolioSerializer(portfolios, many=True)
		return Response(serializer.data)	

	def create(self, request):
		serializer = PortfolioSerializer(data=request.data)
		if serializer.is_valid(): 
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		try:
			portfolio = Portfolio.objects.get(pk=pk)
		except Portfolio.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = PortfolioSerializer(portfolio)
		return Response(serializer.data)

	def update(self, request, pk=None):
		try:
			portfolio = Portfolio.objects.get(pk=pk)
		except Portfolio.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = PortfolioSerializer(portfolio, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		try:
			portfolio = Portfolio.objects.get(pk=pk)
		except Portfolio.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		portfolio.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class TeamViewSet(viewsets.ViewSet):
	def list(self, request):
		teams = Team.objects.all()
		serializer = TeamSerializer(teams, many=True)
		return Response(serializer.data)	

	def create(self, request):
		serializer = TeamSerializer(data=request.data)
		if serializer.is_valid(): 
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		try:
			team = Team.objects.get(pk=pk)
		except Team.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = TeamSerializer(team)
		return Response(serializer.data)

	def update(self, request, pk=None):
		try:
			team = Team.objects.get(pk=pk)
		except Team.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = TeamSerializer(team, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		try:
			team = Team.objects.get(pk=pk)
		except Team.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		team.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PostingViewSet(viewsets.ViewSet):
	def list(self, request):
		postings = Posting.objects.all()
		serializer = PostingSerializer(postings, many=True)
		return Response(serializer.data)	

	def create(self, request):
		serializer = PostingSerializer(data=request.data)
		if serializer.is_valid(): 
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		try:
			posting = Posting.objects.get(pk=pk)
		except Posting.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = PostingSerializer(posting)
		return Response(serializer.data)

	def update(self, request, pk=None):
		try:
			posting = Posting.objects.get(pk=pk)
		except Posting.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = PostingSerializer(posting, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		try:
			posting = Posting.objects.get(pk=pk)
		except Posting.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		posting.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)