from django.urls import path, include
from ewebsite import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('highlight', views.HighlightViewSet, base_name='highlight')
urlpatterns = router.urls