from feed.models import Bookmark,Tag
from .models import Follow
#utils

def is_following(current_user,user):
    return current_user.followed.filter(followed_id=user).count()>0


def follow_status(user):
    followers=Follow.objects.filter(followed_id=user).all()
    followeds=Follow.objects.filter(follower_id=user).all()

    follower_usernames=[]
    for follower in followers:
        follower_usernames.append(follower.follower_id)

    followed_usernames=[]
    for followed in followeds:
        followed_usernames.append(followed.followed_id)  

    return follower_usernames,followed_usernames   


def follow_usernames(followers,followeds):

    follower_usernames=[]
    for follower in followers:
        follower_usernames.append(follower.follower_id)

    followed_usernames=[]
    for followed in followeds:
        followed_usernames.append(followed.followed_id)  

    return follower_usernames,followed_usernames

def user_bookmarks(user):
    bookmark_list=[]
    bookmarks=Bookmark.objects.filter(user_id=user).order_by('-timestamp').all()
    for bookmark in bookmarks:
        bookmark_list.append(bookmark.feed_id)

    return bookmark_list


def tagged_feeds(user):
    tag_list=[]
    tags=Tag.objects.filter(tagged_id=user).order_by('-timestamp').all()
    for tag in tags:
        tag_list.append(tag.feed_id)

    return tag_list