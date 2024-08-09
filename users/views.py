from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from drf_spectacular.utils import extend_schema

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import check_password, make_password

from .serializers import CreatUserSerializer, CustomUserSerializer, ModifyUserSerializer
from .models import CustomUser

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
@extend_schema(
    request=CreatUserSerializer,
    responses=CustomUserSerializer
)
@api_view(['POST'])
def user_register_view(request):
    data = request.data
    
    # if 'password' in data and data['password']:
    #     data['password'] = make_password(data['password'])

    serializer = CreatUserSerializer(data=data)

    if serializer.is_valid():

        # handle unique username
        try:
            serializer.save(password=make_password(data['password']))

        except IntegrityError:
            raise serializers.ValidationError({"username": ["This username already exists."]})
        
        serialized_user = CustomUserSerializer(serializer.data)
        return Response(serialized_user.data, status=status.HTTP_201_CREATED)
    
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# get logged user details and modify them
# /user/me/
@extend_schema(
        request=ModifyUserSerializer,
        responses=CustomUserSerializer
)
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def my_view(request):

    # get current user
    try:
        current_user_data = CustomUser.objects.get(pk=request.user.id)
        
    except CustomUser.DoesNotExist:
        return Response(
            {"message": "user does not found!"},
            status=status.HTTP_404_NOT_FOUND
        )

    # get's user data
    if request.method == "GET":
        serializer = CustomUserSerializer(current_user_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # modifies user data
    if request.method == 'PUT':

        user_upadate_data = request.data

        # set instence with new data
        serializer = ModifyUserSerializer(instance=current_user_data, data=user_upadate_data)

        if serializer.is_valid():

            old_password = user_upadate_data['old_password']
            new_password = user_upadate_data['new_password']

            # checks new password with the old one currently saved in db
            if old_password and new_password and not check_password(old_password, current_user_data.password):

                return Response(
                    {"message"  :"New password is mismatching with the current password!"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer.save(password=make_password(new_password))
            serialized_user = CustomUserSerializer(serializer.data)

            return Response(serialized_user.data, status=status.HTTP_205_RESET_CONTENT)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get user by id
# /user/<user_id>/
@extend_schema(responses=CustomUserSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):

    # check if there's any user with the given id
    try:
        user = CustomUser.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return Response({'error': f'user id: {user_id} does not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    serialized_user = CustomUserSerializer(user)
    return Response(serialized_user.data)

