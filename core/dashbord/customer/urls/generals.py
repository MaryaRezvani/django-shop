from django.urls import path, include
from .. import views


urlpatterns = [

    path("home/", views.CustomerDashbordHomeView.as_view(), name="home"),
]
