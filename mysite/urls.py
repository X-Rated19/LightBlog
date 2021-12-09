from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('quote/', views.quote_list, name='quote_list'),
    path('quote/create/', QuoteCreate.as_view(), name='quote_create'),
    path('quote/<str:slug>', QuoteDetail.as_view(), name='quote_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<str:slug>', PostDetail.as_view(), name='post_detail'),
    path('<str:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('quote/<str:slug>/update/', QuoteUpdate.as_view(), name='quote_update'),
    path('<str:slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('quote/<str:slug>/delete/', QuoteDelete.as_view(), name='quote_delete'),
]