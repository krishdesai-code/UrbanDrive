from django.urls import path
from . import views

urlpatterns = [
    path("",views.admin_login,name="adminlogin"),
    path("home/",views.admin_home,name="admin_home"),
]
