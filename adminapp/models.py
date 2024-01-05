from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profileadmin(models.Model):
    customeruser = models.ForeignKey(User, null = False, blank = False, on_delete=models.CASCADE)
    phone_field = models.CharField(max_length=12, blank = True, null = True)
    image = models.ImageField(upload_to="profile/", max_length=200,blank=True,default="profile/profile.png")
    wallpaper = models.ImageField(upload_to="wallpaper/", max_length=200,blank=True,null = True,default="wallpaper/wallpaper.jpg")
    about_me = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return self.customeruser.username 