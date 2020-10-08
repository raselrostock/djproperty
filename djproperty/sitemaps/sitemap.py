from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.shortcuts import reverse

from listings.models import Listing
from realtors.models import Realtor


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changfreq = 'daily'

    def items(self):
        return ['pages:about']

    def location(self, item):
        return reverse(item)


class ListingSitemap(Sitemap):
    changfreq = 'daily'
    priority = 0.9

    def items(self):
        return Listing.objects.all().order_by('-list_date')

    def location(self, item):
        # return reverse('courses:course-detail', args=[item.slug])
        return reverse('listings:listing', kwargs={"listing_id": item.pk})


class RealtorSitemap(Sitemap):
    changfreq = 'daily'
    priority = 0.9

    def items(self):
        return Realtor.objects.all().order_by('-hire_date')

    def location(self, item):
        # return reverse('realtors:course-detail', args=[item.slug])
        return reverse('realtors:realtor-detail', kwargs={"realtor_slug": item.slug})
