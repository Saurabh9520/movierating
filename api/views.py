from django.shortcuts import render
from .models import Movie,Rating
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status
from api.serializers import MovieSerializer,RatingSerializer
from django.contrib.auth.models import User

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True,methods=['POST'])
    def rate_movie(self,request,pk=None):
        if 'stars' in request.data:



            movie = Movie.objects.get(id=pk)
            stars =request.data['stars']
            User= User.objects.get(id=1)
            print('movie title',movie.title)
            print('user',user.username)

            try:
                rating =Rating.objects.get(user=user.id,movie=movie.id)
                rating.stars =stars
                rating.save()
                serializer = RatingSerializer(rating,many=False)
                response={'message':'rating updated','result':serializer.data}
                
                return Response(response,status=status.HTTP_200_OK)
            except:
                Rating.objects.create(user=user,movie=movie,stars=stars)
                serializer = RatingSerializer(rating,many=False)
                response={'message':'rating updated','result':serializer.data}
                return Response(response,status=status.HTTP_200_OK)
                
            
        else:
            response = {"mes":"you need to provide stars"}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

        
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
