from django.db import models
from djongo import models
import uuid

# Create your models here.
class Report(models.Model):
    title = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class ReportEntry(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    report = models.EmbeddedModelField(
        model_container=Report
    )
