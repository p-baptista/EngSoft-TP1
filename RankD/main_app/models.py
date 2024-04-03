from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    icon_path = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.username}'

class Game(models.Model):
    name = models.CharField(max_length=255)
    studio = models.CharField(max_length=255)
    release_date = models.DateField()
    cover_path = models.CharField(max_length=255, blank=True)
    mean_rating = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

class Platform(models.Model):
    name = models.CharField(max_length=255)
    slang = models.CharField(max_length=5)
    
    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField()
    rating =models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    
    def __str__(self):
        return f'{self.game} review by {self.user.username}'

class FriendList(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_lists_as_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_lists_as_user2')
    
    def __str__(self):
        return f'{self.user1.name} - {self.user2.name}'
    