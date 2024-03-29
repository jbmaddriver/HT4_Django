from django.shortcuts import render
from django.template.context_processors import request
from . import models
from django.http import HttpResponse, HttpRequest, request
from django.http import  QueryDict
from django.template import loader
from .models import Student, Students100
from faker import Faker
fake = Faker()


# Generate user using Faker. PATH..../generate-student/

def gen_student(request):
    student = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),age=fake.random_int(min=18, max=45, step=1))
    template = loader.get_template('gen_student.html')
    context = {'student': student}
    return HttpResponse(template.render(context, request))


# Generate users using Faker with query parameters from URL link. Example: PATH....generate-students/?number=15

def gen_students100(request):
    query = request.GET.get('num')
    query_number = int(query)
    if 0 < query_number <= 100:
        gen_number = query_number
        student_list = []
        for s in range(gen_number):
            temp_arg = Students100.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),age=fake.random_int(min=18, max=45, step=1))
            student_list.append(temp_arg)
        all_students = student_list
        template = loader.get_template('gen_students100.html')
        context = {'student100': all_students}
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(f'Wrong number, please enter "num" integer value between 1 and 100. See example: ".../?num=100"')

