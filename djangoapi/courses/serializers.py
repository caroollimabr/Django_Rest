from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):  # serializer: translates our data to and from JSON
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')  # itens que surgem obrigatoriamente + o q esta na Model
        