from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from faker import Faker
from rest_framework import serializers
from typing import Any

from users.serializers import CreatUserSerializer

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass
    
    def handle(self, *args: Any, **options):
        faker = Faker()
        for i in range(10):

            user_data = {
                "username":faker.user_name(),
                "first_name":faker.first_name(),
                "last_name":faker.last_name(),
                "email":faker.email(),
                "password":"Pass123!"
            }
            user_serializer = CreatUserSerializer(data=user_data)

            if user_serializer.is_valid():
               # handle unique username
                try:
                   user_serializer.save()
                   print(f"{i}: user saved {user_serializer.validated_data["username"]}")

                except IntegrityError:
                    print(f"error: {user_serializer.validated_data["username"]} already exsists!")
                    raise serializers.ValidationError({"username": ["This username already exists."]})
            else:
              print(f"user_serializer does not valid!")
                    
        


