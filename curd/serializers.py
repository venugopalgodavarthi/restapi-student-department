from rest_framework import serializers
from curd.models import employee, student,department

class curdserializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields= '__all__' 

class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields= '__all__' 

class departserializers(serializers.ModelSerializer):
    class Meta:
        model = department
        fields= '__all__' 
