from django.db import models

class Post(models.Model):
    topic = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic