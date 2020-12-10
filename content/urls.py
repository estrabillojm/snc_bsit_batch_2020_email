from django.urls import path
from . import views

app_name="content"

urlpatterns = [
    path('create/', views.content_create, name="create"),
    path('create/<id>', views.content_create, name="create"),
    path('list/', views.content_list, name="list"),
    path('list/', views.content_list, name="list"),
    path('dNUGnnVwy9zQyIkigk9D6vtoSBqhyM9jSS1IiT1fU/<int:id>', views.content_delete, name="delete"),
]
