from rest_framework import serializers
from .models import Movie, MovieReview, Actor, Director
# from django.core.serializers import Serializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' 

class MovieReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = MovieReview
        fields = '__all__'

