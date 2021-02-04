from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    age = models.IntegerField()
    
def __repr__(self):
    return f"User: {self.id} - {self.name} "