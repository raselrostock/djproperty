from django.urls import path

from pages.views.home import home
from pages.views.about import about
from pages.views.faqs import faqView

app_name = 'pages'

urlpatterns = [
    path('', home, name='index'),
    path('about', about, name='about'),
    path('faqs', faqView, name='faqs')
]
