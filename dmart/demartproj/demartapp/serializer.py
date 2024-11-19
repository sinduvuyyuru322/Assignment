from rest_framework import serializers
from .models import product_details,customer_details,Order
class  product_detailsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = product_details  # Specify the model
        fields = '__all__'  #

        
class customer_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer_details
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'quantity', 'quantity_price', 'total_amount']

    def create(self, validated_data):
        # Get the product object from the product ID
        product = validated_data['product']
        quantity = validated_data['quantity']

        # Calculate quantity_price and total_amount
        quantity_price = product.price * quantity
        total_amount = quantity_price  # If you want to add more logic to calculate total amount, adjust this

        # Create the order instance
        order = Order.objects.create(
            customer=validated_data['customer'],
            product=product,
            quantity=quantity,
            quantity_price=quantity_price,
            total_amount=total_amount
        )

        return order