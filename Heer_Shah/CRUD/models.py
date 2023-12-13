from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)


    def _str_(self):
        return self.name
