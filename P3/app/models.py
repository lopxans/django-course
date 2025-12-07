from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  
    # If the User is deleted → all their Posts are also deleted.
    # (Use when posts should not exist without the user.)

    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    # If the User is deleted → prevent deletion.
    # (Use when you must keep the User as long as posts exist.)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # If the User is deleted → set user field to NULL.
    # (Use when posts can stay even after user is deleted.)
    
    title = models.CharField(max_length=255)

    
