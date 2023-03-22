from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.translator,name="trans"),
    path('translate/',views.translated,name="translate")
]