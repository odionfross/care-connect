from django.shortcuts import render

def index(request):
    # retrieve info for the home page
    return render(request, 'index.html')