from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def print_hello(request):
    movie_details={
        'title':'godfather',
        'year':1990,
        'summary':'story of an underworld king',
        'sucess':True
    }
    return render(request,'hello.html',movie_details,)
