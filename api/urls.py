"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from ewebsite.views import HighlightViewSet, ServiceViewSet, TextModalViewSet, PortfolioViewSet, TeamViewSet, PostingViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'highlight/', HighlightViewSet)
router.register(r'service/', ServiceViewSet)
router.register(r'textmodal/', TextModalViewSet)
router.register(r'portfolio/', PortfolioViewSet)
router.register(r'team/', TeamViewSet)
router.register(r'posting/', PostingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


