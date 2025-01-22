from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['violet evergarden', 
                   'arcane series', 
                   'haikyuu!']
    }
    return render(request, 'movies/index.html', context) 

def about(request):
    return render(request, 'movies/about.html') 
# HttpResponse('My Fav Movies')

# app/templates/app/index.html
# movies/templates/movies/index.html

# {} is also known as context