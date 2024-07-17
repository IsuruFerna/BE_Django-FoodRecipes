from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view




# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/user/api/token',
        '/user/api/token/refresh'
    ]
    return Response(routes)

def index(request):
    return JsonResponse({"message": "hello world!"})

def login_view(request):
    pass

def logout_view(request):
    pass