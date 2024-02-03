from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.IntegerField()
    #profile_picture = models.OneToOneField(Profile_Pic, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.ImageField()
    caption = models.TextField()
    timeCreated = models.DateTimeField()
    # on delete cascade means if we delete the user, the blog post will be deleted too
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    # if I want to display this post as a string, use this function
    def __str__(self): 
        return self.title + ' | ' + self.author.username

