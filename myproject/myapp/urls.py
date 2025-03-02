
from django.urls import path,include
from .import views

urlpatterns = [
    
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about")
]
