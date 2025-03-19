from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)      #blank=True means image is not required, it's ok if you don't provide one.

    def __str__(self):      #method that we can call on the model
        return self.title