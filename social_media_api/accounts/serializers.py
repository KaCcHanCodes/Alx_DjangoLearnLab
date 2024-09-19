from rest_framework import serializers
from .models import CustomUser
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, instance):
        if instance['password1'] != instance['password2']:
            raise ValidationError({'message': "Both passwords must match"})
        
        email = CustomUser.objects.filter(email=instance['email'])
        if email.exists():
            raise ValidationError({'message': "Email already taken!"})
        
        return instance
    
    def create(self, validated_data):
        passwrd = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(passwrd)
        user.save()
        Token.objects.create(user=user)

        return user
    
class CustomUserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']