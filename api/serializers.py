from rest_framework import serializers
from .models import Movie,Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','director')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields=('id','star','user','movie')