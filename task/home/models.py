from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Status(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status

class Task(models.Model):
    name = models.CharField(max_length=30)
    details = models.TextField() 
    para = models.TextField()
    date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

