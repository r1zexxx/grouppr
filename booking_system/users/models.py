from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Booking(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creater = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.author})"
    
class Rooms(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
