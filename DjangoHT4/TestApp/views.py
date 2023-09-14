from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.


def Hello_world(request):
    return HttpResponse("Hello_world!")


def render_list(request):
    all_users = Member.objects.all().values()
    template = loader.get_template('list.html')
    context = {
        'users': all_users,
        }
    return HttpResponse(template.render(context, request))
