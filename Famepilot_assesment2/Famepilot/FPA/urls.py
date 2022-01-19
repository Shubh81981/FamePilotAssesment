from .views import Profile_list
from django.urls import path
from . import views


urlpatterns = [
    path('profile/',Profile_list),
    path('register/',views.register,name="register"),
    path('',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('data',views.data,name="data"),
    path('add_data/',views.add_data,name="add_data")



]
