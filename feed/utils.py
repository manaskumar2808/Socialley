from django.contrib.auth.models import User
from users.models import Follow
from .models import Feed,Like,Comment,Tag

def has_liked(user):
    liked_feeds=[]

    current_user=User.objects.filter(id=user.id)
    user_likes=Like.objects.filter(liker_id__in=current_user).all()

    for user_like in user_likes:
        liked_feeds.append(user_like.feed_id) 

    return liked_feeds

def has_liked_comments(user):
    liked_comments=[]

    current_user=User.objects.filter(id=user.id)
    user_likes=Like.objects.filter(liker_id__in=current_user).all()

    for user_like in user_likes:
        liked_comments.append(user_like.comment_id)

    return liked_comments
    

def feed_comments(feed):
    current_feed=Feed.objects.filter(id=feed.id)
    feed_comments=Comment.objects.filter(feed_id__in=current_feed).order_by('-date_commented').all()
    return feed_comments


def tagged_users(user,feed):
    tagged_usernames=[]
    tags=Tag.objects.filter(tagger_id=user,feed_id=feed).all()
    for tag in tags:
        tagged_usernames.append(tag.tagged_id)

    return tagged_usernames
