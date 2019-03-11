from rest_framework import serializers
from .models import Tickets, Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)

class TicketsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tickets
        fields = ('id', 'description', 'stage', 'category', 'created_date',)



