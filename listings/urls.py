from django.urls import path 
from listings.views.index_view import index
from listings.views.listing_view import listing
from listings.views.search_view import search 

app_name = 'listings'

urlpatterns = [
    path('', index, name='listings'),
    path('<int:listing_id>', listing, name='listing'),
    path('search', search, name='search')
]
