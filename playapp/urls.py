from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order/<int:product_id>/", views.order_view, name="order_view"),
    path("submit_order/", views.submit_order, name="submit_order"),

]

