
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', crud),
    path('delete/<id>', t_delete,name="delete"),
    path('complete/<id>', t_complete,name="complete"),
   
]
