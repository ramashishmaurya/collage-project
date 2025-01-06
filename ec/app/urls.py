from django.urls import path
from app import views
urlpatterns = [
    path("", views.index , name='index'),
    path("contact",views.contact ),
    path("about",views.about),
]