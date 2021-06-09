from rest_framework import serializers
from geekapi.models import Person


class GeekapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','email')