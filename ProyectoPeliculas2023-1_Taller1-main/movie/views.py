from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

def home(request):
    searchTerm = request.GET.get ('searchMovie')
    if searchTerm:
        movies = Movie.object.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})


def about(request):
    return render(request, 'about.html')

