from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField()
    date_subscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class NewsletterContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
