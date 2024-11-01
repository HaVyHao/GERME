from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('search/', views.search, name="search"),
    path('detail/', views.detail, name="detail"),
    path('category/', views.category, name="category"),
    path('introduce/', views.introduce, name="introduce"),
    path('pay/', views.pay, name="pay"),
    path('payqr/', views.payqr, name="payqr"),
    path('founder/', views.founder, name="founder"),
    path('logout/', views.logoutPage, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),
    path('update_item/',views.updateitems, name="update_item"),
]
