from rest_framework import serializers
from administration.models import Class

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'