from django.urls import path
from . import views

app_name = "computergrid"
urlpatterns = [
    path("", views.index, name="index"),
]
