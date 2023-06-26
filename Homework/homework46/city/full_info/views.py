from django.shortcuts import render, get_object_or_404
from .models import Full_info


def full_info(request):
    full_info = Full_info.objects.all()
    return render(request, 'full_info/full_info.html', {'full_info': full_info})


def detail(request, info_id):
    info = get_object_or_404(Full_info, pk=info_id)
    return render(request, 'full_info/detail.html', {'info': info})

# Create your views here.
