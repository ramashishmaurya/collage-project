from django.urls import path 
from authcart import views

urlpatterns = [
    path("signup/",views.signup , name='signup'),
    path("login/",views.handlelogin , name='handlelogin'),
    path("logout/",views.handlelogout , name='handlelogout'),
    path("blog/" , views.blog , name='blog'),
    path("about/" , views.blog , name='blog'),
    
]
