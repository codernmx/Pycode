"""myWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
		# path('admin/', admin.site.urls),
		url(r'^$', views.index),
		# url(r'index/', views.index),
		# url(r'get$', views.get),
		# url(r'post$', views.post),
		url(r'fanyi/baidu/translate/word$', views.translate),#字词翻译
		url(r'fanyi/baidu/translate/img$', views.translateFile),#图片翻译
		url(r'get/pdf/change/token$', views.getChangePdfToken),#pdf转文件换取token
		url(r'get/file/url$', views.tokenGetFileUrl),#token下载文件
		url(r'get/change/pdf/token$', views.getPdfChangeToken), #文档转pdf换取token
]

