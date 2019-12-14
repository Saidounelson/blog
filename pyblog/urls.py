from django.conf.urls import url
from django.contrib import admin
from pyblog import views

urlpatterns = [
    url(r'^post/',views.post_list,'home'),
]