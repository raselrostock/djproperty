from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404 
from listings.models import Listing
from listings.choices import state_choices, price_choices, bedroom_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    per_page = 6 
    paginator = Paginator(listings, per_page)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)