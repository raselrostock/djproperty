"""djproperty URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView

# Sitemap
from django.contrib.sitemaps.views import sitemap
from djproperty.sitemaps.sitemap import StaticViewSitemap, ListingSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'listings': ListingSitemap,
}


urlpatterns = [
    # Robots.txt
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('listings/', include('listings.urls', namespace='listings')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('realtors/', include('realtors.urls', namespace='realtors'))
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)