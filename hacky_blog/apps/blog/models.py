from django.db import models
from django.utils import timezone # timezone module from django built-in packages

# Create your models here.
class Post(models.Model):
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types
    author = models.ForeignKey('auth.User') # one author, multiple posts 
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title