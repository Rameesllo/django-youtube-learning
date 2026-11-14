from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {
        'name': 'ramees',
        'destination': destinations
    })


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    res = val1 + val2

    return render(request, 'result.html', {'result': res})


destinations = [
    {
        'name': 'Kerala',
        'desc': 'Gods Own Country',
        'price': 5000,
        'img': 'kerala.jpg'
    },
    {
        'name': 'Goa',
        'desc': 'Beautiful Beaches',
        'price': 7000,
        'img': 'goa.jpg'
    },
    {
        'name': 'Kashmir',
        'desc': 'Paradise on Earth',
        'price': 10000,
        'img': 'kashmir.jpg'
    }
]