from django.urls import path 
from realtors import views

app_name = 'realtors'

urlpatterns = [
    path('', views.RealtorListView, name='realtor-list'),
    path('<str:realtor_slug>', views.RealtorDetailView.as_view(), name='realtor-detail')
]