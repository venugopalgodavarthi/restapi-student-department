from student.models import *
from rest_framework import serializers, fields


class departmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = department
        fields = ('id', 'dept_name', 'dept_head',)


class studentSerializer(serializers.ModelSerializer):
    departments = departmentSerializer(many=True)

    class Meta:
        model = student
        fields = ('id', 'first_name', 'last_name', 'departments')

    def create(self, validated_data):
        albums_data = validated_data.pop('departments')
        stu = student.objects.create(**validated_data)
        for album_data in albums_data:
            department.objects.create(depart=stu, **album_data)
        return stu

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('departments')
        albums = (instance.departments).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.dept_name = album_data.get('dept_name', album.dept_name)
            album.dept_head = album_data.get('dept_head', album.dept_head)
            album.save()
        return instance