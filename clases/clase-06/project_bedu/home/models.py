from django.db import models

class Post(models.Model):
    """docstring for Post."""
    title = models.CharField(max_length=140)
    content = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# runserver
