from django.urls import path,include
from . import views

app_name = "dashbord"

urlpatterns = [
    path("home/",views.DashbordHomeView.as_view(),name="home"),
    
    # include admin urls
    path("admin/",include('dashbord.admin.urls')),
    
    # include customer urls
    path("customer/",include('dashbord.customer.urls')),
]


