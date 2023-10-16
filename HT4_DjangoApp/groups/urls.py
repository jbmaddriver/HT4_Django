from django.urls import path
from . import views

urlpatterns = [

    path('', views.output_groups, name='output_groups')

]
