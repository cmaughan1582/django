from django.shortcuts import render
from django.http import HttpResponse
import time


def index(request):
    return HttpResponse("Hello World. The time is currently " + time.strftime("%c"))
