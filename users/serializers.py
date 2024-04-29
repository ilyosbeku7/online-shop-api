from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
import random
from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework.validators import ValidationError

class UserSerializer(ModelSerializer):
    confirmation_code = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'confirmation_code')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.confirmation_code = random.randint(100000, 999999)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.confirmation_code = validated_data.get('confirmation_code', instance.confirmation_code)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user=authenticate(user=username, password=password)

        if user is None:
            data={
                'status': False,
                "message":"parol xato kiritildi"
            }
            raise ValidationError(data)
        
        return attrs