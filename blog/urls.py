from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog_index, name="blog_index"),
    path("blog/<int:pk>", blog_detail, name="blog_detail"),
    path("contact/", contact, name="contact"),
]