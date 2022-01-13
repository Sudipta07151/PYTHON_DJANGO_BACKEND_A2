from rest_framework import serializers


from .models import Users
from .models import ModelsList
from .models import PdfList


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'username', 'password', 'date_joined']

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)


class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelsList
        fields = '__all__'


class PdfSerializers(serializers.ModelSerializer):
    class Meta:
        model = PdfList
        fields = '__all__'
