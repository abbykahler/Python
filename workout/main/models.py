from django.db import models
from django import forms

# # our new form
# class ContactForm(forms.Form):
#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     content = forms.CharField(
#         required=True,
#         widget=forms.Textarea
#     )

#     def login_validator(self, post_data):
#         errors = {}
#         if len(post_data['email']) < 8:
#             errors['email'] = "Email must be 8 characters or more!"
#         if len(post_data['password']) < 8:
#             errors['password'] = "Password must be 8 characters or more!"
#         return errors
    
    
# class User(models.Model): 
#     first_name = models.CharField(max_length=55)
#     last_name = models.CharField(max_length=55)
#     email = models.EmailField(max_length=55)
#     password = models.CharField(max_length=55)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = UserManager()



