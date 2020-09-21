'''# posts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

class Rating(models.Model):
    Movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    star = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])



    '''
# posts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

class Rating(models.Model):
    Movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    star = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])



    