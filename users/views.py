from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer, ModifyUserSerializer
from .models import CustomUser
from .utils import ResponseUser

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
@api_view(['POST'])
def user_register_view(request):
    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():

        user = serializer.save()

        # removes password from the validated data and adds user_id to send as a response
        user_data = serializer.validated_data
        del user_data["password"]
        user_data['id'] = user.id

        return Response({"message": "user successfully saved into the database", "data": user_data}, status=status.HTTP_201_CREATED)
    
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def my_view(request):
    user_data = request.user

    # get's user data
    if request.method == "GET":
        userRespone = ResponseUser(
            user_data.id, 
            user_data.username,
            user_data.first_name,
            user_data.last_name,
            user_data.email
        )

        return Response(userRespone.__dict__, status=status.HTTP_200_OK)
    
    # modifies user data
    if request.method == 'PUT':
        user_old_data = CustomUser.objects.get(pk=user_data.id)

        # set instence with new data
        serializer = ModifyUserSerializer(user_old_data, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



def index(request):
    return Response({"message": "hello world!"})

