from django.shortcuts import render,redirect
from .models import Books
from rest_framework import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import BookSerailizers
from rest_framework import status
# Create your views here.
"""def create(request):
    return render(request,'home.html')"""
def Postdetails(self,request):
    if request.method == "POST":
       serializer = BookSerailizers(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def getbooks(self,request,pk):
    if request.method == "GET":
        getbooks = Books.objects.get(pk= pk)
        serializer = BookSerailizers(getbooks, many=True)
        return Response(serializer.data)

def updatebooks(self,request,pk):
    getbooks = Books.objects.get(pk = pk)
    serializer = BookSerailizers(getbooks, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)
def deletebook(request,id):
    delbook = Books.objects.get(id=id)
    delbook.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)









