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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, BlogSitemap

from django.contrib import admin
from django.urls import include, path, re_path
from .views import about, advertising, workforus, contact, faq, feedback, contributors_guide, complaints, terms, privacy, cookies, contributors 
from newsletter.views import newsletter

sitemaps = {
    'pages': StaticViewSitemap,
    'post': BlogSitemap,
}

urlpatterns = [
    path('about-us/', about, name='about'),
    path('advertising/', advertising, name='advertising'),
    path('workforus/', workforus, name='workforus'),
    path('contact-us/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('feedback/', feedback, name='feedback'),
    path('contributors-guide-and-contacts/', contributors_guide, name='contributors_guide'),
    path('complaints-and-corrections/', complaints, name='complaints'),
    path('terms-of-service/', terms, name='terms'),
    path('privacy-policy/', privacy, name='privacy'),
    path('cookies-policy/', cookies, name='cookies'),
    path('contributors/', contributors, name='contributors'),    
    path('newsletter/', newsletter, name='newsletter'),

    url(r'^sitemap\.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('tg/admin/', admin.site.urls),

    path('', include('posts.urls', namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)