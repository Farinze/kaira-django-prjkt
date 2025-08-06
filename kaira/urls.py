from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root of the app — this is what gets included above
]
