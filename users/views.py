from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework import exceptions as rest_exceptions
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiExample

from .models import UserAccount
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
)
from includes.drf.serializers import APIResponseSerializer

@extend_schema_view(
    create_user=extend_schema(
        tags=['Users'],
        request=UserCreateSerializer,
        responses={
            201: APIResponseSerializer,
        },
        description='Creates a new user with the provided email if it does not exist in the database.',
        summary='Create new user with email',
        examples=[
            OpenApiExample(
                'Successful Response',
                value={
                    'success': True,
                    'message': 'User created successfully',
                    'data': {
                        'email': 'user@example.com',
                        'first_name': None,
                        'last_name': None,
                        'age': None
                    }
                },
                response_only=True,
                status_codes=['201']
            ),
        ]       
    ),
    update_user=extend_schema(
        tags=['Users'],
        request=UserUpdateSerializer,
        responses={
            200: APIResponseSerializer,
        },
        description='Updates an existing user with the provided fields. Only updates fields that are provided.',
        summary='Update existing user details',
        examples=[
            OpenApiExample(
                'Successful Update',
                value={
                    'success': True,
                    'message': 'User updated successfully',
                    'data': {
                        'email': 'existing@example.com',
                        'first_name': 'John',
                        'last_name': 'Doe',
                        'age': 30
                    }
                },
                response_only=True,
                status_codes=['200']

            ),
        ]
            )
    )

class UserViewSet(viewsets.GenericViewSet):
    queryset = UserAccount.objects.all()

    @action(detail=False, methods=['post'], url_path='create')
    def create_user(self, request: Request)-> Response:
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserSerializer(user).data
        response_data = {
            'success': True,
            'message': 'User created successfully',
            'data': user_data
        }
        return Response(APIResponseSerializer(response_data).data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['patch'], url_path='populate')
    def update_user(self, request: Request) -> Response:
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = UserAccount.objects.get(email=serializer.validated_data.get('email'))
            update_data = {k: v for k, v in serializer.validated_data.items() if k != 'email'}
            user.update_fields(**update_data)
            user_data = UserSerializer(user).data
            response_data = {
                'success': True,
                'message': 'User updated successfully',
                'data': user_data
            }
            return Response(APIResponseSerializer(response_data).data, status=status.HTTP_200_OK)
        except self.queryset.model.DoesNotExist:
            raise rest_exceptions.NotFound('User not found. Complete signup first.', status=status.HTTP_404_NOT_FOUND)