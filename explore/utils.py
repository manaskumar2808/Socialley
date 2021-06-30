from users.models import Follow

def is_following(user):
    follow_list=[]
    follows=Follow.objects.filter(follower_id=user.id).all()
    for follow in follows:
        follow_list.append(follow.followed_id)
    return follow_list

def followers(user):
    follower_list=[]
    follows=Follow.objects.filter(followed_id=user.id).all()
    for follow in follows:
        follower_list.append(follow.follower_id)
    return follower_list
