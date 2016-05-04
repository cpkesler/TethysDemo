from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/home.html', context)

def info(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/info.html', context)

def map(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/map.html', context)