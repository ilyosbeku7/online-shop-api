from rest_framework import serializers
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100, min_length=4)
    password=serializers.CharField(min_length=4)





class UserSerializer(serializers.ModelSerializer):
    # We don't want to expose the password field
    password = serializers.CharField(write_only=True)
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    def create(self, validated_data):
        # Use Django's create_user function to create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
           
        )
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password'  )