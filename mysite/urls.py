from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('quote', views.quote_list, name='quote_list'),
    path('quote/<str:title>/', QuoteDetail.as_view(), name='quote_detail'),
    path('<str:title>', PostDetail.as_view(), name='post_detail'),
]