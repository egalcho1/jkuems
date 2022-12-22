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
]
