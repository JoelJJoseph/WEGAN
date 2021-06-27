from django.db import models

# Create your models here.
class Causedby(models.Model):
    title  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Solution(models.Model):
    causedby = models.ForeignKey(Causedby, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    solution = models.TextField(max_length=8000)

    def __str__(self):
        return self.title