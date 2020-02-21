# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse
from datetime import datetime

from posts.models import Post

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['about', 'advertising', 'workforus', 'contact', 'faq', 'feedback', 'contributors_guide', 'complaints', 'terms', 'privacy', 'cookies', 'contributors' ]

    def lastmod(self, item):
    	return datetime.now()

    def location(self, item):
        return reverse(item)


class BlogSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return Post.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.publish

    def location(self, obj):
    	return '/'