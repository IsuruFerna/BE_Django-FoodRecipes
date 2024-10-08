from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from django.core import exceptions
import django.contrib.auth.password_validation as validator

from .models import CustomUser

# decode user data with JWT
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class CreatUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        password = attrs.get('password')
        user = self.instance
        errors = dict()
        
        #password validation
        try:
            # validate the password and catch the exception
            validator.validate_password(password=password, user=user)
        
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
            raise serializers.ValidationError(errors)

        return attrs
            
class ModifyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    old_password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'old_password', 'new_password']

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')

        user = self.instance
        errors = dict()

        # validate new password
        if new_password:
            try:
                # validate the password and catch the exception
                validator.validate_password(password=new_password, user=user)
            
            except exceptions.ValidationError as e:
                errors['new_password'] = list(e.messages)
                raise serializers.ValidationError(errors)
                
        return attrs