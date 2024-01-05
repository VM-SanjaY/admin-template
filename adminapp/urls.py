from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name="adminlogin"),
    path('register/',views.adminregister,name="adminregister"),
    path('logout/',views.adminlogout,name="adminlogout"),
    path('home/',views.adminhome,name = 'adminhome'),
    path('table/',views.admintable,name="admintable"),
    path('table-edit/',views.admintableedit,name="admintableedit"),
    path('profile/',views.adminprofile,name="adminprofile"),
    path('profile/edit/',views.editprofile,name="editprofile"),
    
]