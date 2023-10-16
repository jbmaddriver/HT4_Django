from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.template import loader
from .models import Group


# Create your views here.


def output_groups(request):
    all_students = Group.objects.all().values()
    template = loader.get_template('output_groups.html')
    context = {'groups': all_students}
    return HttpResponse(template.render(context, request))