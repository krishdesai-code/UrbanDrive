from django.urls import path
from . import views

urlpatterns = [
    path("",views.admin_login,name="adminlogin"),
    path("home/",views.admin_home,name="admin_home"),
    path("addnew/",views.add_car,name="add_car"),
    path("allcar/",views.allcar,name="allcar"),
    path("allcar/update/<int:id>",views.Update_car,name="update"),
    path("allcar/delete/<int:id>",views.Delete_car,name="delete"),
]
