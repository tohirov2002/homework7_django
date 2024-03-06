from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse(
        '<div style="display: flex;align-items: center;justify-content:center;gap: 30px;">'
        '<a href="http://127.0.0.1:8000/" style="font-size: 32px;text-decoration: none;">Home<a>'
        '<a style="margin: 20px;text-decoration: none;font-size: 32px;" href="http://127.0.0.1:8000/about">About<a>'
        '<a style="margin: 20px;text-decoration: none;font-size: 32px;" href="http://127.0.0.1:8000/contact">Contact<a>'
        '<a style="margin: 20px;text-decoration: none;font-size: 32px;" href="http://127.0.0.1:8000/login">Login<a>'
        '<a style="margin: 20px;text-decoration: none;font-size: 32px;" href="http://127.0.0.1:8000/register">Register<a>'
        '<div>'
    )


def about(request):
    return HttpResponse(
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000">Orqaga<a><p>'
        '<p>Xush kelibsiz <a href="http://127.0.0.1:8000/contact/">About<a> pagemizga!<p>'
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000/contact/">Oldinga<a><p>'
    )


def contact(request):
    return HttpResponse(
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000/about/">Orqaga<a><p>'
        '<p>Xush kelibsiz <a href="http://127.0.0.1:8000/contact/">Contact<a> pagemizga!<p>'
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000/login/">Oldinga<a><p>'
    )


def login(request):
    return HttpResponse(
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000/contact/">Orqaga<a><p>'
        '<p>Xush kelibsiz <a href="http://127.0.0.1:8000/login/">Login<a> pagemizga!<p>'
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000/register/">Oldinga<a><p>'
    )


def register(request):
    return HttpResponse(
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000/login/">Orqaga<a><p>'
        '<p>Xush kelibsiz <a href="http://127.0.0.1:8000/register/">Register<a> pagemizga!<p>'
        '<p><a style="text-decoration: none;" href="http://127.0.0.1:8000">Oldinga<a><p>'
    )