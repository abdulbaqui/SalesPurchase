from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index',views.index, name ="index"),
    path('Signinuser',views.Signinuser, name ="Signinuser"),
    path('Registration',views.Registration, name ="Registration"),
    path('logoutuser',views.logoutuser, name ="logout"),
    path('sales', views.sales, name="sales"),
    path('purchase', views.purchase, name="purchase"),
    path('Customer', views.Customer_Dropdown, name="Customer"),
    path('FormCreation',views.FormCreation,name="FormCreation"),
]