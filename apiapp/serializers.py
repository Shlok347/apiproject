from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

class MasterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MasterProfile
        fields = '__all__'
