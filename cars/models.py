from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    about= models.TextField()

    def __str__(self):
        return self.name
