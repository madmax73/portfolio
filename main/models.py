from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bullet_points = models.TextField(help_text="Enter bullet points separated by newline")
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.title