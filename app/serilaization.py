from app.models import *
from rest_framework import serializers
class StudentMS(serializers.ModelSerializer):
    class meta:
        model=Student
        fields='__all__'