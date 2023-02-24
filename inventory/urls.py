
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from inventory.views import CategoryView, ItemListView,ItemDetailView,CategoryDetailView


urlpatterns = [

    path('items/',ItemListView.as_view(),name='itemlist'),
    path('category/',CategoryView.as_view(),name='category'),
    path('items/<int:item_id>/', ItemDetailView.as_view(),name='item_detail'),
    path('category/<int:cat_id>/', CategoryDetailView.as_view(),name='cat_detail'),
]
