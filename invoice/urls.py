from django.urls import path
from .import views 
urlpatterns=[
    path('customer_home_page',views.customer_home_page,name='customer_home_page'),
    path('customer_reg',views.customer_reg,name='customer_reg'),
    path('item_master',views.item_master,name='item_master')

]