from multiprocessing import context
from sqlite3 import Date
from django.shortcuts import render
from members.models import Person
from datetime import datetime

def create_person(request):
    new_person = Person.objects.create(name = 'Fabricio Abati', relationship ='Hermano más pequeño', age = 14, creation_date = datetime.now().day)
    context = {
        'new_person': new_person
    }
    return render(request, 'new_person.html', context=context)


def list_members(request):
    members = Person.objects.all()
    context = {
        'members': members
    }
    return render(request, 'members_list.html', context=context)