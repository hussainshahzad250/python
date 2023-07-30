from rest_framework import serializers
from tutorials.models import Tutorial, Employee


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'title', 'description', 'published')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'email', 'mobile')
