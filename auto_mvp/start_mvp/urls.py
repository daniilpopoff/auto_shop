from django.urls import path
from . import views

# app_name = 'start_mvp'
urlpatterns =[
     path('', views.BaseView.as_view(), name='base_view'),
     path('contact', views.ContactView.as_view(), name='contact_view'),
     path('about/', views.AboutView.as_view(), name='about_us_view'),
     path('car_list/', views.CarListView.as_view(),name='car_list'),
     path('car_list/<int:id>', views.CarDetailView.as_view(), name='car_detail'),
     path('car_list/<int:id>/delete', views.CarDeleteView.as_view(), name='car_delete'),
     path('car_list/<int:id>/update', views.CarUpdateView.as_view(), name='car-update'),
     path('create_car/', views.CarCreateView.as_view()),
     path('search/', views.search_results, name='search'),
     # path('search_gpt/', views.car_search_gpt, name='car_search'),#car_serch был рабочий
]
