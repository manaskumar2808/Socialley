from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=60,null=True,blank=True)
    phonenum=models.BigIntegerField('Phone Number',null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)

    image=models.ImageField('Upload Photo',default='default_profile.jpg',upload_to='profile_pics')


    def __str__(self):
        return f"Profile({self.user.username},{self.name})"



class Follow(models.Model):
    follower_id=models.ForeignKey(User,related_name='followed',on_delete=models.CASCADE)
    followed_id=models.ForeignKey(User,related_name='follower',on_delete=models.CASCADE)

    def __str__(self):
        return f"Follow({self.follower_id},{self.followed_id})"
