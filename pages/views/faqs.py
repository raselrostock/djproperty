from django.shortcuts import render

from listings.models import Listing


def faqView(request):
    listings = Listing.objects.order_by('-list_date').all()[:3]
    context = {
        'title': 'FAQS',
        'listings': listings
    }
    return render(request, 'pages/faqs.html', context)
