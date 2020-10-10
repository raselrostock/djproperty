"""djproperty URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView

# Errors
from django.conf.urls import (
    handler400,
    handler403,
    handler404,
    handler500
)

# Sitemap
from django.contrib.sitemaps.views import sitemap
from djproperty.sitemaps.sitemap import StaticViewSitemap, ListingSitemap, RealtorSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'listings': ListingSitemap,
    'realtors': RealtorSitemap
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

handler400 = 'djproperty.views.bad_request'
handler403 = 'djproperty.views.permission_denied'
handler404 = 'djproperty.views.not_found'
handler500 = 'djproperty.views.server_error'

# if settings.DEBUG == True:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)