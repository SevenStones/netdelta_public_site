"""ndwww URL Configuration

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
import www.views
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', www.views.index, name='home'),
    #url(r'^admin/', admin.site.urls),
    url(r'^thanks/', www.views.thanks),
    url(r'^error/', www.views.error),
    url(r'^sitemap/', www.views.sitemap),
]
handler404 = 'www.views.handler404'
handler500 = 'www.views.handler500'