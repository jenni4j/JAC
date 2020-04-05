from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Assets(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.CharField(max_length=200)
    balance = models.TextField()
    last_update_date = models.DateTimeField(default=timezone.now)
    save_date = models.DateTimeField(blank=True, null=True)

    def save_input(self):
        self.save_date = timezone.now()
        self.save()

    def __str__(self):
        return self.account
        