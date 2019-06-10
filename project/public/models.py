from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorites(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()

class Commentaries(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.IntegerField(default=5)
    movie_id = models.IntegerField(null=True)
