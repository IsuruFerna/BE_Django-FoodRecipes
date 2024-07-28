from faker import Faker
from rest_framework.pagination import PageNumberPagination

# paginator response for meal views
def paginator_response(data, request, Serializer):
    
    # sets pagination using django_rest and it's global settings from the settings.py file under REST_FRAMEWORK list
    paginator = PageNumberPagination()
    paginated_data = paginator.paginate_queryset(data, request)
    serialized_data = Serializer(paginated_data, many=True)

    return paginator.get_paginated_response(serialized_data.data)

# generates users for unit test
def user_generator():
    faker = Faker()
    return {
        'email': faker.email(),
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'username': faker.user_name(),
        'password': faker.password()
    }
