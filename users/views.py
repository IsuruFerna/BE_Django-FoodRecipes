from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import CustomUserSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/user/api/token',
        '/user/api/token/refresh',
        '/user/register/'
    ]
    return Response(routes)

# register user 
# /user/register/
"""
{
    "username": username,
    "first_name": firstName,
    "last_name": lastName,
    "email": email,
    "password": password,
}
"""
@api_view(['POST', 'GET'])
def user_register_view(request):
    serializer = CustomUserSerializer(data=request.data)

    if request.method == "GET":
        print("this is req: " + repr(serializer))
        return Response(repr(serializer))

    if serializer.is_valid():

        user = serializer.save()

        # removes password from the validated data and adds user_id to send as a response
        user_data = serializer.validated_data
        del user_data["password"]
        user_data['id'] = user.id

        return Response({"message": "user successfully saved into the database", "data": user_data}, status=status.HTTP_201_CREATED)
    
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return JsonResponse({"message": "hello world!"})

def login_view(request):
    pass

def logout_view(request):
    pass