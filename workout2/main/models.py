from django.db import models

class Workout(models.Model):
    exercise = models.CharField(max_length=200)
    # muscle = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='cars').ImageField(upload_to='cars')
    set1 = models.IntergerField()
    # set2 = models.IntergerField()
    # set3 = models.IntergerField()
    # set4 = models.IntergerField()
    # set5 = models.IntergerField()
    # set6 = models.IntergerField()
    reps = models.IntergerField()
    lbs = models.IntergerField()
    id = models.IntergerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
