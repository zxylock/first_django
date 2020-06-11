from django.db import models
import datetime,time

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_created=False, default=datetime.datetime.now)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_created=False, default=datetime.datetime.now)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + ".."