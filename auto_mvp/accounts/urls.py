from django.urls import path
from .import  views



urlpatterns=[
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('admin_register/',views.admin_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('personal_card/',views.ProfileView.as_view(), name='profile'),

]