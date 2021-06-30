from django.db import models
from users.models import User
from datetime import datetime

# Create your models here.

class Status(models.Model):
    setter=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField('Caption',max_length=30)
    image=models.ImageField(upload_to='status_images',null=True,blank=True)
    video=models.FileField(upload_to='status_videos',null=True,blank=True)
    timestamp=models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"Status({self.setter,self.caption})"
    