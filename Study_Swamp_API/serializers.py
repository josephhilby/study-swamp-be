from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'

    def get_user_type(self, obj):
        return obj.get_user_type_display()