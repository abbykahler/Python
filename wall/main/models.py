from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 3: 
            errors['first_name'] = "First name must be 3 characters or more!"
        if len(post_data['last_name']) < 3: 
            errors['last_name'] = "Last name must be 3 characters or more!"    
        if len(post_data['username']) < 3:
                errors['username'] = "Username Field is Required"
        if len(post_data['password']) < 8: 
            errors['password'] = "Password must be 4 characters or more!"
        if post_data['password'] != post_data['confirm_password']: 
            errors['confirm'] = "Passwords don't match!"    
        return errors   
            
    def login_validator(self,post_data):
        errors = {}
        if len(post_data['email']) < 8: 
            errors['email'] = "Email must be 8 characters or more!"
        if len(post_data['password']) < 8: 
            errors['password'] = "Password must be 4 characters or more!"
        return errors   
    
    def login_authenticate(self, name, password):
        users_with_username = self.filter(username=name)
        if not users_with_username:
            return False 
        
        
class User(models.Model): 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
class Messages(models.Model): 
    message = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='messages', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    
    
class Comment(models.Model): 
    comment = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    message = models.ForeignKey(Messages, related_name='comments_in_message', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)