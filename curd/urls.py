from django.urls import path
from curd.views import *
urlpatterns= [
    path(r'curdlist/',curd_list,name="curd_list"),
    path(r'curddetail/<pk>/',curd_detail,name="curd_detail"),
    path(r'curd/<pk>/',curd,name="curd"),
    
    path(r'deptlist/',dept_list,name="dept_list"),
    path(r'deptdetail/<pk>/',dept_detail,name="dept_detail"),
    path(r'dept/<pk>/',dept,name="dept"),
    
    path(r'studentlist/',student_list,name="student_list"),
    path(r'studentdetail/<pk>/',student_detail,name="student_detail"),
    path(r'student/<pk>/',student,name="student"),
]