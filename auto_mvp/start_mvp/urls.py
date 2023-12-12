from django.urls import path
from . import views

urlpatterns =[
     path('base/', views.BaseView.as_view(), name='base_view'),
     path('car_list/', views.CarListView.as_view(),name = "car_list"),
     path('car_list/<int:id>', views.CarDetailView.as_view(), name="car_detail"),
     path('car_list/<int:id>/delete', views.CarDeleteView.as_view()),
     path('car_list/<int:id>/update', views.CarUpdateView.as_view()),
     path('create_car/', views.CarCreateView.as_view()),
     path('search/', views.search, name='search'),
]
