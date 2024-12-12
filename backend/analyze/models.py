from django.db import models

class DetectedObjects(models.Model):
    user_id = models.IntegerField()
    object_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user_id', 'object_name')
