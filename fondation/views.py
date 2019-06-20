# -*- coding: utf-8 -*-

from django.shortcuts import render

#create your views here

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'pages/about-us/about-us.html')

def about_ceo(request):
    return render(request, 'pages/about-ceo/about-ceo.html')

def gallerie(request):
    return render(request, 'pages/gallerie/gallerie.html')

def team(request):
    return render(request, 'pages/team/team.html')

def formation(request):
    return render(request, 'pages/formation/formation.html')

def bibliotheque(request):
    return render(request, 'pages/bibliotheque/bibliotheque.html')


def error404(request, exception=404):
    data = {}
    return render(request, 'pages/errors/404.html', data, status=404)

def error500(request, exception=500):
    data = {}
    return render(request, 'pages/errors/500.html', data, status=500)