from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('quote', views.quote_list, name='quote_list'),
]