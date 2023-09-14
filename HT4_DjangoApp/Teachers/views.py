from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.template import loader
from .models import Teachers_list

# Create your views here.


def output_teachers(request):
    all_students = Teachers_list.objects.all().values()
    template = loader.get_template('output_teachers.html')
    context = {'teachers': all_students}
    return HttpResponse(template.render(context, request))