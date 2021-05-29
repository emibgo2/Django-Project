
from django.contrib import admin
from django.urls import path,include
import functioncrud.urls
import functioncrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',functioncrud.views.welcome, name = "welcome"),
    path('functioncrud/',include(functioncrud.urls)),

]
