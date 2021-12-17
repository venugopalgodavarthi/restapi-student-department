
from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from curd.models import department,student
from curd.serializers import curdserializers,departserializers,studentserializers
from rest_framework import generics
from rest_framework.decorators import api_view
import asyncio 
from asgiref.sync import sync_to_async 
from aiohttp import web 
@api_view(['GET', 'POST','PUT', 'DELETE'])
def curd_list(request):
    emp=None
    if request.method == 'GET':
        emp = student.objects.all()
        name = request.query_params.get('first_name', None)
        if name is not None:
            emp = emp.filter(name__icontains=name)
        
        curd_serializer = curdserializers(emp, many=True)
        return JsonResponse(curd_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        curd_data = JSONParser().parse(request)
        curd_serializer = curdserializers(data=curd_data)
        if curd_serializer.is_valid():
            curd_serializer.save()
            return JsonResponse(curd_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(curd_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = student.objects.all().delete()
        return JsonResponse({'message': '{} curd were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET','PUT', 'DELETE'])
def curd_detail(request,pk):
    try: 
        emp = student.objects.get(pk=pk) 
    except student.DoesNotExist: 
        return JsonResponse({'message': 'The record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        curd_serializer = curdserializers(emp) 
        return JsonResponse(curd_serializer.data) 
    
    if request.method == 'PUT': 
        curd_data = JSONParser().parse(request) 
        curd_serializer = curdserializers(emp, data=curd_data) 
        if curd_serializer.is_valid(): 
            curd_serializer.save() 
            return JsonResponse(curd_serializer.data) 
        return JsonResponse(curd_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        curd.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
      
@api_view(['GET'])
def curd(request,pk):
    emp = student.objects.filter(name=pk)
    if request.method == 'GET': 
        curd_serializer = curdserializers(emp, many=True)
        return JsonResponse(curd_serializer.data, safe=False)
    
    
    
@api_view(['GET', 'POST','PUT', 'DELETE'])
def dept_list(request):
    dept=None
    if request.method == 'GET':
        dept = department.objects.all()
        name = request.query_params.get('dept_name', None)
        if name is not None:
            dept = dept.filter(name__icontains=name)
        
        depart_serializers = departserializers(dept, many=True)
        return JsonResponse(depart_serializers.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        dept_data = JSONParser().parse(request)
        depart_serializers = curdserializers(data=dept_data)
        if depart_serializers.is_valid():
            depart_serializers.save()
            return JsonResponse(depart_serializers.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(depart_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = department.objects.all().delete()
        return JsonResponse({'message': '{} curd were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET','PUT', 'DELETE'])
def dept_detail(request,pk):
    try: 
        dept = department.objects.get(pk=pk) 
    except department.DoesNotExist: 
        return JsonResponse({'message': 'The record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        dept_serializer = departserializers(dept) 
        return JsonResponse(dept_serializer.data) 
    
    if request.method == 'PUT': 
        dept_data = JSONParser().parse(request) 
        dept_serializer = departserializers(dept, data=dept_data) 
        if dept_serializer.is_valid(): 
            dept_serializer.save() 
            return JsonResponse(dept_serializer.data) 
        return JsonResponse(dept_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        curd.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
      
@api_view(['GET'])
def dept(request,pk):
    dept = department.objects.filter(name=pk)
    if request.method == 'GET': 
        dept_serializer = departserializers(dept, many=True)
        return JsonResponse(dept_serializer.data, safe=False)
    
    


@api_view(['GET', 'POST','PUT', 'DELETE'])
def student_list(request):
    stu=None
    if request.method == 'GET':
        emp = student.objects.all()
        name = request.query_params.get('first_name', None)
        if name is not None:
            stu = stu.filter(name__icontains=name)
        
        stu_serializer = studentserializers(stu, many=True)
        return JsonResponse(stu_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        stu_data = JSONParser().parse(request)
        stu_serializer = studentserializers(data=stu_data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return JsonResponse(stu_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(stu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = student.objects.all().delete()
        return JsonResponse({'message': '{} curd were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET','PUT', 'DELETE'])
def student_detail(request,pk):
    try: 
        stu = student.objects.get(pk=pk) 
    except student.DoesNotExist: 
        return JsonResponse({'message': 'The record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        stu_serializer = studentserializers(stu) 
        return JsonResponse(stu_serializer.data) 
    
    if request.method == 'PUT': 
        stu_data = JSONParser().parse(request) 
        stu_serializer = studentserializers(stu, data=stu_data) 
        if stu_serializer.is_valid(): 
            stu_serializer.save() 
            return JsonResponse(stu_serializer.data) 
        return JsonResponse(stu_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        curd.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
      
@api_view(['GET'])
def student(request,pk):
    stu = student.objects.filter(name=pk)
    if request.method == 'GET': 
        stu_serializer = studentserializers(stu, many=True)
        return JsonResponse(stu_serializer.data, safe=False)

