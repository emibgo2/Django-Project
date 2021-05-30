
from django.contrib import admin
from django.urls import path,include
import functioncrud.urls
import functioncrud.views
import classcrud.urls
import classcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',classcrud.views.BlogView.as_view(), name = "welcome"),
    path('functioncrud/',include(functioncrud.urls)),
    path('classcrud/', include(classcrud.urls))

]
