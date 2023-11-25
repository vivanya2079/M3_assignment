from django.urls import path
from . import views

urlpatterns = [
    path('print_hello/', views.print_hello, name='print_hello'),
]
