from rest_framework import serializers

class APIResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField(read_only=True)
    message = serializers.CharField(read_only=True)
    data = serializers.SerializerMethodField(read_only=True)

    def get_data(self, obj) -> dict:
        return obj.get('data')
    def to_representation(self, instance) -> dict:
        data = instance.get('data')
        if isinstance(data, serializers.Serializer):
            data = data.data
        return {
            'success': instance.get('success'),
            'message': instance.get('message'),
            'data': data
        }