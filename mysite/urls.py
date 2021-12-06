from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('quote', views.quote_list, name='quote_list'),
    path('quote/create/', QuoteCreate.as_view(), name='quote_create'),
    path('quote/<str:slug>', QuoteDetail.as_view(), name='quote_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<str:slug>', PostDetail.as_view(), name='post_detail'),
]