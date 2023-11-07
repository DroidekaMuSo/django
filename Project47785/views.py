from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hi Django - Coder")


def welcome_html(request):
    return HttpResponse("<b> Hi Django </b> - Coder")


def welcome_name(request, name):
    return HttpResponse(f"<h1>{name}</h1> <b>Hola Django</b>")