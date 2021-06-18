from django.db import models
from django.conf import settings
from django.conf.urls.static import static

# # Create your models here.

# class TvManager(models.Manager):
#     def show_validator(self, post_data):
#         errors = {}
#         if len(post_data['title']) < 2:
#             errors['title'] = "Title too short"
#         if len(post_data['network']) < 2:
#             errors['network'] = "Network name is too short"
#             if len(post_data['description']) < 10:
#                 errors['description'] = "Description name is too short"
#         return errors



# class Show(models.Model): 
#     title = models.CharField(max_length=255)
#     network = models.CharField(max_length=25)
#     release_date = models.DateTimeField()
#     description = models.CharField(max_length=25)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = TvManager()