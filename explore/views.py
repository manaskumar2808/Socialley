from django.shortcuts import render
from django.contrib.auth.models import User
from feed.models import Feed
from .utils import is_following,followers

# Create your views here.
def people(request):
    accounts=User.objects.all()
    feeds=Feed.objects.all()
    context={
        'title':'EXPLORE',
        'accounts':accounts,
        'feeds':feeds,
        'follow_list':is_following(request.user),
        'follower_list':followers(request.user),
    }
    return render(request,'explore/explore.html',context)