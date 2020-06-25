from rest_framework import serializers
from guardian.models import Guardian

class GuardianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guardian
        fields = '__all__'
