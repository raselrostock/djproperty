from django.shortcuts import render
from listings.models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices

def home(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)