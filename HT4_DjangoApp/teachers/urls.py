from django.urls import path
from . import views

urlpatterns = [

    path('', views.output_teachers, name='output_teachers'),

]
