"""rbac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('perm/', include('perm.urls')),
    path('perm_api/', include('perm_api.urls')),
    path('excel/', include('django_excel_to_db.urls')),
    path('datatable/', include('datatable.urls')),
    path('api/oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
