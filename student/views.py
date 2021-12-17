from django.shortcuts import render
from student.models import *
from student.serializers import *
from rest_framework import generics
# Create your views here.


class studentListView(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer


class studentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = studentSerializer
    queryset = student.objects.all()


class departmentListView(generics.ListCreateAPIView):
    queryset = department.objects.all()
    serializer_class = departmentSerializer


class departmentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = departmentSerializer
    queryset = department.objects.all()