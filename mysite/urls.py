from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('quote', views.quote_list, name='quote_list'),
    path('quote/<str:title>/', views.quote_detail, name='quote_detail'),
    path('<str:title>', views.post_detail, name='post_detail'),
]