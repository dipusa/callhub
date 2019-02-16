from django.db import models
import uuid

# Create your models here.


class Sequence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    series = models.CharField(max_length=252)
    created_at = models.DateTimeField(auto_now=True)
