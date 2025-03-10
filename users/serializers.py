from rest_framework import serializers
from .models import UserAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email', 'first_name', 'last_name', 'age', 'date_created', 'date_updated']
        read_only_fields = ['date_created', 'date_updated']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email']
        
    def validate_email(self, value) -> str:
        if UserAccount.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return value
    
    def create(self, validated_data) -> UserAccount:
        user = UserAccount.objects.create(
            email=validated_data['email'],  
        )
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    age = serializers.IntegerField(required=False, allow_null=True, min_value=0)
    
    class Meta:
        model = UserAccount
        fields = ['email', 'first_name', 'last_name', 'age']
        
    def validate_email(self, value) -> str:
        if not UserAccount.objects.filter(email=value).exists():
            raise serializers.ValidationError("User not found. Complete signup first.")
        return value

    def validate_age(self, value) -> int:
        if value < 0:
            raise serializers.ValidationError("Age must be a positive number.")
        if value == 0:
            raise serializers.ValidationError("Age must be greater than 0.")
        return value
        
    def update(self, instance, validated_data) -> UserAccount:
        email = validated_data.pop('email', None)
        
        instance.update_fields(**validated_data)
        
        return instance