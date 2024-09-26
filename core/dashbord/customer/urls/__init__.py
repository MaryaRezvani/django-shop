from django.urls import path,include

app_name = "customer"

urlpatterns = [
    path("",include("dashbord.customer.urls.generals")),
    path("",include("dashbord.customer.urls.profiles")),
]


