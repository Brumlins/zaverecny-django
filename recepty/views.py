from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def recepty(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def members_list(request):
    members = Member.objects.all()
    return render(request, 'members_list.html', {'members': members})
