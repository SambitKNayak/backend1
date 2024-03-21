from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', { 'movies': movies })
    
    # movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)

    # Movie.objects.all()
    # # select * from movies_movie
    # Movie.objects.filter(release_year=2024)
    # # select * from movies_movie where ...
    # Movie.objects.get(id=1)