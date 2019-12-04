"""laba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^enword/', include('laba.api.enword.urls', namespace='enword')),
    url(r'^rusword/', include('laba.api.rusword.urls', namespace='rusword')),
    url(r'^api/', include('laba.api.urls', namespace='api')),
    url(r'laba', include('laba.urls', namespace='laba')),
    url('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url('admin/', admin.site.urls),
]
