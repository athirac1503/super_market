from django.urls import path
from .import views
urlpatterns=[
    path('vendor_home_page',views.vendor_home_page,name='vendor_home_page'),
]