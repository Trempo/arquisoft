from rest_framework import serializers

from paymentmethods.models import PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['order', 'name', 'username', 'accountnumber', 'date', 'cvc']
