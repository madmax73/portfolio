from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/',default=None)
    link = models.URLField()

    def __str__(self):
        return self.title