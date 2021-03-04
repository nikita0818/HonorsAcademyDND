from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('initial/', views.initial),
    path('final/', views.final),
    # path('index/', views.index, name="index"),

] 