"""telegraph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('world/', views.world, name='world'),
    path('nigeria/', views.nigeria, name='nigeria'),
    path('politics/', views.politics, name='politics'),
    path('opinion/', views.opinion, name='opinion'),
    path('sport/', views.sport, name='sport'),
    path('business/', views.business, name='business'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('<cat_slug>/<slug>/', views.detail, name='detail'),
    path('create/', views.post_create, name='create'),
    path('<cat_slug>/<slug>/edit/', views.post_update, name='update'),
    path('<cat_slug>/<slug>/delete/', views.post_delete, name='delete'),

    # url(r'^create/$', post_create, name='create'),
    # url(r'^(?P<cat_slug>[\w-]+)/(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<cat_slug>[\w-]+)/(?P<slug>[\w-]+)/delete/$', post_delete),
    # url(r'^(?P<cat_slug>[\w-]+)/(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]
