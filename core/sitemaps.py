from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from shop.models import Product

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return [
            'core:home',
            'core:about',
            'core:gallery',
            'core:contact',
            'core:privacy',
            'core:terms',
            'core:shipping',
            'shop:product_list',
        ]

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Product.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('shop:product_detail', args=[obj.pk])
