from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from ewebsite.models import Highlight
from ewebsite.serializers import HighlightSerializer

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
