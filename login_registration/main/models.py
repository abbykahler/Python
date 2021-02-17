from django.db import models


class UserManager(models.Manager):

    def register_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 3: 
            errors['name'] = "Name must be 3 characters or more!"
        if len(post_data['alias']) < 3: 
            errors['alias'] = "Alias  must be 3 characters or more!"
        if len(post_data['email']) < 8: 
            errors['email'] = "Email must be 8 characters or more!"
        if len(post_data['password']) < 8: 
            errors['password'] = "Password must be 4 characters or more!"
        if post_data['password'] != post_data['confirm_password']: 
            errors['confirm'] = "Passwords don't match!"
        return errors

    def login_validator(self, post_data):
        errors = {}
        if len(post_data['email']) < 8:
            errors['email'] = "Email must be 8 characters or more!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be 8 characters or more!"
        return errors
    
class User(models.Model): 
    name = models.CharField(max_length=55)
    alias = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # def __repr__(self):
    #     return f'{self.first_name} {self.last_name} {self.email} {self.password}'



class Author(models.Model):  
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
class Book(models.Model): 
    title = models.CharField(max_length=55)
    author = models.ForeignKey(Author, related_name='books',on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, related_name='submitted_books',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
class Review(models.Model): 
    content = models.CharField(max_length=55)
    rating = models.CharField(max_length=55)
    book = models.ForeignKey(Book, related_name='reviews',on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name='submitted_reviews',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)