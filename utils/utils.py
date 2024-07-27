from rest_framework.pagination import PageNumberPagination

def paginator_response(data, request, Serializer):
    
    # sets pagination using django_rest and it's global settings from the settings.py file under REST_FRAMEWORK list
    paginator = PageNumberPagination()
    paginated_data = paginator.paginate_queryset(data, request)
    serialized_data = Serializer(paginated_data, many=True)

    return paginator.get_paginated_response(serialized_data.data)