from django.shortcuts import render
from realtors.models import Realtor

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    som = Realtor.objects.filter(is_som=True).first()
    context = {
        'realtors': realtors,
        'som': som
    }
    return render(request, 'pages/about.html', context)