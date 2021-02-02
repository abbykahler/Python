from django.db import models



class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 3: 
            errors['first_name'] = "First name must be 3 characters or more!"
        if len(post_data['last_name']) < 3: 
            errors['last_name'] = "Last name must be 3 characters or more!"
        if len(post_data['email']) < 8: 
            errors['email'] = "Email must be 8 characters or more!"
        if len(post_data['password']) < 8: 
            errors['password'] = "Password must be 4 characters or more!"
        if post_data['password'] != post_data['confirm_password']: 
            errors['confirm'] = "Passwords don't match!"
        return errors
    
class User(models.Model): 
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    objects = UserManager()
    
    
    