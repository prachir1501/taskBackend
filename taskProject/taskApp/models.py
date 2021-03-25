from django.db import models

# Create your models here.

class Tasks(models.Model):
    primaryid=models.TextField()
    status=models.CharField(max_length=200)

def __str__(self):
    return '%s %s' % (self.primaryid, self.status)
