from django.urls import path,include

app_name = "admin"

urlpatterns = [
    path("",include("dashbord.admin.urls.generals")),
    path("",include("dashbord.admin.urls.profiles")),
    path("",include("dashbord.admin.urls.products")),

]

