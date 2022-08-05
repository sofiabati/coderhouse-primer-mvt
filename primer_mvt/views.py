from errno import EADDRNOTAVAIL
from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html', context={})