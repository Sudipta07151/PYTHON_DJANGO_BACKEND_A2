from rest_framework import serializers


from .models import Users
from .models import ModelsList


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'username', 'password']
    
    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)

class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelsList
        fields = '__all__'
