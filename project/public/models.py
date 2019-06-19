from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import formats

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


class Contact(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at',]

    def __str__(self):
        if self.user_id is None:
            username = "Anonymous"
        else:
            username = self.user_id.username
        return "Ticket du " + str(formats.date_format(self.created_at, "SHORT_DATETIME_FORMAT")) + " de " + username
