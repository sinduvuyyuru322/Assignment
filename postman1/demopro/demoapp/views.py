from django.shortcuts import render
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Employee
from django.http import JsonResponse

# Create your views here.s
@api_view(["POST","GET"])
def employee_list(request):
    if request.method == "POST":
        serialiser = EmployeeSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data,status = status.HTTP_201_CREATED)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        employess = Employee.objects.all()
        serialiser = EmployeeSerializer(employess,many = True)
        return JsonResponse({"empolyee_list" : serialiser.data})
    