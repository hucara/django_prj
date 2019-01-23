from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    is_train = models.BooleanField(default = False)
    label = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
