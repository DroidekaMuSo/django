from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("Hi Django - Coder")


def welcome_html(request):
    return HttpResponse("<b> Hi Django </b> - Coder")


def welcome_name(request, name):
    return HttpResponse(f"<h1>{name}</h1> <b>Hola Django</b>")


def greeting_template(request):
    context = {
        "name": "Diego",
        "age": 34,
        "children": [
            {
                "name": "Cynthia",
                "age": 34
            },
            {
                "name": "Ian",
                "age": 5
            },
            {
                "name": "Regina",
                "age": 8
            }
        ]
    }
    return render(request, "index.html", context)
