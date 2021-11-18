from rest_framework import serializers

from orderitems.models import OrderItem


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'name', 'price', 'quantity']