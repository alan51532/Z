from django.shortcuts import render
from django.http import JsonResponse
import pygame

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def uan(request):
    return render(request, 'main/uan.html')

def uan2(request):
    return render(request, 'main/uan2.html')
def uan3(request):
    return render(request, 'main/uan3.html')
def uan4(request):
    return render(request, 'main/uan4.html')
