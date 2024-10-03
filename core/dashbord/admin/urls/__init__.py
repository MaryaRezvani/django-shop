from django.urls import path,include

app_name = "admin"

urlpatterns = [
    path("",include("dashbord.admin.urls.generals")),
    path("",include("dashbord.admin.urls.profiles")),
    path("",include("dashbord.admin.urls.products")),
    path("",include("dashbord.admin.urls.orders")),
    path("",include("dashbord.admin.urls.reviews")),
    path("",include("dashbord.admin.urls.newsletters")),
    path("",include("dashbord.admin.urls.contacts")),
    path("",include("dashbord.admin.urls.users")),
    path("",include("dashbord.admin.urls.coupons")),

]


