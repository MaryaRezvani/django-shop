from django.urls import path, include
from .. import views


urlpatterns = [

    path("home/", views.AdminDashbordHomeView.as_view(), name="home"),
]
