from django.db import models
from django import forms


class Profile_Pic(models.Model):
    title = models.CharField(max_length=200)
    pic = models.ImageField()
    timeCreated = models.DateTimeField()

    def __str__(self): 
        return self.pic.url

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.IntegerField()
    profile_picture = models.OneToOneField(Profile_Pic, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
class Friend(models.Model):
    # primary key is a field that can uniquely distinguish a row in a table
    # such as ID
    id = models.AutoField(primary_key=True)

    # foreign key means this value links to a value in another table, in User table
    # on_delete CASCADE means if one user doesn't exist anymore, this entry will be deleted
    # CASCADE 层叠
    userA = models.ForeignKey(User, on_delete=models.CASCADE)
    friendName = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timeCreated = models.DateTimeField()
    # on delete cascade means if we delete the user, the blog post will be deleted too
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    # if I want to display this post as a string, use this function
    def __str__(self): 
        return self.title + ' | ' + self.author.username

