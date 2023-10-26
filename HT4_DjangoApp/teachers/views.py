from django.http import HttpResponse
from django.template import loader
from .models import Teacher


def output_teachers(request):
    all_students = Teacher.objects.all().values()
    template = loader.get_template("output_teachers.html")
    context = {"teachers": all_students}
    return HttpResponse(template.render(context, request))
