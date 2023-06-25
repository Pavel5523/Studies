from django.shortcuts import render


def full_info(request):
    return render(request, 'full_info/full_info.html')

# Create your views here.
