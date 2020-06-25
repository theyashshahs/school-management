from rest_framework import serializers
from authentication.models import Auth

class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auth
        fields = '__all__'

