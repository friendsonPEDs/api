from rest_framework import serializers
from .models import Steps

class StepsSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Map serializers fields to the model fields"""
        model = Steps
        fields = ('date_created', 'date_modified', 'date_start', 'date_end', 'steps', 'owner')
        read_only_fields = ('date_created', 'date_modified', 'owner')
