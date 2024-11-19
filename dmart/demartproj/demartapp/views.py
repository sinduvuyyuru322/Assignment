from django.shortcuts import render
from .models import product_details,customer_details,Order
from rest_framework import status
from rest_framework.response import Response
from .serializer import  product_detailsSerializer,customer_detailsSerializer,OrderSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
@api_view(["POST","GET"])
def product(request):
    if request.method == "POST":
        serializer = product_detailsSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        product= product_details.objects.all()
        serializer = product_detailsSerializer(product,many =True)
        return Response(serializer.data)
@api_view(['POST','GET'])  
def customer(request):
    if request.method == "POST":
        serializer = customer_detailsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    if request.method == "GET":
        product= customer_details.objects.all()
        serializer = customer_detailsSerializer(product,many =True)
        return Response(serializer.data)

@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        customer_id = request.data.get('customer')
        product_id = request.data.get('product')
        quantity = request.data.get('quantity')

        # Retrieve the customer and product objects
        try:
            customer = customer_details.objects.get(id=customer_id)
            product = product_details.objects.get(id=product_id)
        except customer_details.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        except product_details.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if there is enough stock for the product
        if product.quantity_in_stock < quantity:
            return Response({"error": "Not enough stock available"}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate quantity price and total amount
        quantity_price = product.price * quantity
        total_amount = quantity_price

        # Save the order
        order = Order.objects.create(
            customer=customer,
            product=product,
            quantity=quantity,
            quantity_price=quantity_price,
            total_amount=total_amount
        )

        # Decrease the stock for the product
        product.quantity_in_stock -= quantity
        product.save()

        # Serialize the order and return the response
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)