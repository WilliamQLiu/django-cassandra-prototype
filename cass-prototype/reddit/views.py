from django.shortcuts import render

# Create your views here.


def home(request):
    """ Home View """

    return render(request, 'reddit/main.html')
