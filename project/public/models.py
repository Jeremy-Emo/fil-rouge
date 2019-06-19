from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Favorites(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()

    class Meta:
        verbose_name = 'Favori'
        verbose_name_plural = 'Favoris'

class Commentaries(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie_id = models.IntegerField(null=True)
    text = models.TextField(null=False, blank=True, default="")

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'
