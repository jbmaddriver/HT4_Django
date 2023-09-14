from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.template import loader
from .models import Groups_list


# Create your views here.


def output_groups(request):
    all_students = Groups_list.objects.all().values()
    template = loader.get_template('output_groups.html')
    context = {'groups': all_students}
    return HttpResponse(template.render(context, request))