from rest_framework import serializers
from administration.models import Class, Fee

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'

class FeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fee
        fields = '__all__'