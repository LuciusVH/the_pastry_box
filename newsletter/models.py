from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField()
    date_subscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class NewsletterContent(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
