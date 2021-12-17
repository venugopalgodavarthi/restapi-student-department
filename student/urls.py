from django.urls import path
from student.views import *
urlpatterns=[

path(r'student/', studentListView.as_view()),
path(r'student/(?P<pk>\d+)/', studentView.as_view()),
path(r'department/', departmentListView.as_view()),
path(r'department/(?P<pk>\d+)/', departmentView.as_view()),
]