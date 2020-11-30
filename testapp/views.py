from django.shortcuts import render

# Create your views here.
def Home_View(request):
    return render(request, 'testapp/home.html')

def Movie_View(request):
    return render(request, 'testapp/movie.html')

def Sport_View(request):
    return render(request, 'testapp/sport.html')

def Politics_View(request):
    return render(request, 'testapp/politics.html')