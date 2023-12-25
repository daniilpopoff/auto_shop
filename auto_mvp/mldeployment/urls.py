from django.urls import path
from .views import predict_car_price

urlpatterns = [
    path('predict/', predict_car_price, name='predict_car_price'),
]