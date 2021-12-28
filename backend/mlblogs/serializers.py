from rest_framework import serializers

from .models import Users
from .models import ModelsList

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=ModelsList
        fields='__all__'
