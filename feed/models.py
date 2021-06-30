from datetime import datetime
from django.db import models
from django.urls import reverse
from users.models import User


# Create your models here.
class Feed(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='post_images',null=True,blank=True)
    video=models.FileField(upload_to='post_videos',null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    timestamp=models.DateTimeField(default=datetime.now)
    creator=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feed-detail',kwargs={'pk':self.pk})

    def get_gallery(self):
        return Gallery.objects.filter(feed_id=self).all()

    def has_gallery(self):
        return Gallery.objects.filter(feed_id=self).count()>0

    def get_all_comments(self):
        return Comment.objects.filter(feed_id=self).order_by('-date_commented').all()
    
    def get_recent_comments(self):
        return Comment.objects.filter(feed_id=self).order_by('-date_commented').all()[:2]

    def has_comments(self):
        return Comment.objects.filter(feed_id=self).count()>0
    

class Gallery(models.Model):
    feed_id=models.ForeignKey(Feed,related_name='feed',on_delete=models.CASCADE)
    gallery=models.ImageField(upload_to='post_images',null=True,blank=True)

    def __str__(self):
        return f"Gallery({self.feed_id})"


class Comment(models.Model):
    comment_text=models.CharField(max_length=100)
    date_commented=models.DateTimeField(default=datetime.now)
    feed_id=models.ForeignKey(Feed,related_name='feed_comments',on_delete=models.CASCADE)
    commentor_id=models.ForeignKey(User,related_name='user_comments',on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return f"Comment({self.commentor_id},{self.feed_id})"

    def get_likes(self):
        return Like.objects.filter(comment_id=self).count()


class Like(models.Model):
    feed_id=models.ForeignKey(Feed,related_name='feed_likes',on_delete=models.CASCADE,null=True,blank=True)
    comment_id=models.ForeignKey(Comment,related_name='comment_likes',on_delete=models.CASCADE,null=True,blank=True)
    liker_id=models.ForeignKey(User,related_name='user_likes',on_delete=models.CASCADE)

    def __str__(self):
        return f"Like({self.liker_id},{self.feed_id},{self.comment_id})"



class Bookmark(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    feed_id=models.ForeignKey(Feed,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f"Bookmark({self.user_id},{self.feed_id})"



class Tag(models.Model):
    tagger_id=models.ForeignKey(User,related_name='user_tag',on_delete=models.CASCADE)
    tagged_id=models.ForeignKey(User,related_name='user_tagged',on_delete=models.CASCADE)
    feed_id=models.ForeignKey(Feed,on_delete=models.CASCADE,null=True,blank=True)
    timestamp=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Tag({self.tagger_id},{self.tagged_id},{self.feed_id})"

