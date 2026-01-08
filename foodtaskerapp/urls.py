from django.urls import path
from .views import (
    home, register_view, login_view, logout_view,
    restaurant_account_view, restaurant_meal_view,
    restaurant_order_view, restaurant_report_view
)

urlpatterns = [
    path("", home, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("restaurant/account/", restaurant_account_view, name="restaurant-account"),
    path("restaurant/meal/", restaurant_meal_view, name="restaurant-meal"),
    path("restaurant/order/", restaurant_order_view, name="restaurant-order"),
    path("restaurant/report/", restaurant_report_view, name="restaurant-report"),
]