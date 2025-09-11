from django.shortcuts import render

def catimages_home(request):
    return render(request, 'catimages.html')