from django.urls import path 
from . import views
app_name="emp"
urlpatterns = [
    path('home/',views.home,name="home"),
    path('register/',views.registration,name="register"),
    path('',views.login,name="login"),
    path('emp/',views.emp,name="emp"),
    path('employ/',views.employ,name="employ"),
    path('empd/<int:id>/',views.empd,name="empd"),
    path('eped/<int:id>/',views.eped,name="eped"),
     path('dela/<int:id>/',views.dela,name="dela"),
     path('empr/',views.empr,name="empr"),
     path('atr/',views.atr,name="atr"),
     path('search/',views.search,name="search"),
     path('rupdte/',views.upadte,name="upadte"),
     path('salary/',views.salary,name="salary"),
     path('upsalary/<int:id>/',views.upsalary,name="upsalary"),
     path('users/',views.users,name="users"),
     path('request/',views.request,name="request"),
     path('dlm/<int:id>/',views.dlm,name="dlm"),
    path('logout', views.logout, name='logout'),
    path('profile/',views.profile,name="profile"),
]
