from rest_framework import serializers
from movies.models import Genre
from .models import Poll

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Poll
        fields = '__all__'