from django.urls import path
from . import views

urlpatterns = [
    path("generate-student/", views.gen_student, name="gen_student"),
    path("generate-students/", views.gen_students100, name="gen_students100"),
]
