from rest_framework import serializers
from administration.models import Course, Fees

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class FessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fees
        fields = '__all__'