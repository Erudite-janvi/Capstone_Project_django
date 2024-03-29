from rest_framework import serializers
from .models import login


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = ['username', 'first_name',
                  'last_name', 'phone_number', 'password']
