from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    #Create relationships (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    #add any additional attributes we want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        #built in attribute of django.attrib.auth.models.user !
        return self.user.username