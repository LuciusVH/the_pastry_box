from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class NewsletterContent(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title
