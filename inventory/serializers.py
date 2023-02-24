from dataclasses import fields
from rest_framework import serializers
from . models import Category,Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    items_cat = ItemSerializer(read_only = True,many=True)
    class Meta:
        model = Category
        fields = '__all__'