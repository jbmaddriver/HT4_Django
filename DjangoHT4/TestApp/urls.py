from django.urls import path
from . import views

urlpatterns = [
    path('Test/', views.Hello_world, name='Hello world'),
    path('', views.render_list, name='users_list')
]
