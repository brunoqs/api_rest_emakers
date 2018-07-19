from django.urls import path, include
from ewebsite import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('highlight', views.HighlightViewSet, base_name='highlight')
router.register('service', views.ServiceViewSet, base_name='service')
router.register('textmodal', views.TextModalViewSet, base_name='textmodal')
router.register('portfolio', views.PortfolioViewSet, base_name='portfolio')
router.register('team', views.TeamViewSet, base_name='team')
router.register('posting', views.PostingViewSet, base_name='posting')

urlpatterns = router.urls