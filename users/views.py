from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from feed.models import Feed,Bookmark,Tag
from .models import Follow
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from .utils import is_following,follow_usernames,user_bookmarks,tagged_feeds

# Create your views here.

def registration(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegistrationForm()

    context={
        'form':form
    }
    return render(request,'users/registration.html',context)



@login_required
def profile(request):
    feeds=Feed.objects.filter(creator=request.user).order_by('-timestamp').all()

    followers=Follow.objects.filter(followed_id=request.user).all()
    followeds=Follow.objects.filter(follower_id=request.user).all()

    follower_usernames,followed_usernames=follow_usernames(followers,followeds)
    bookmarks=user_bookmarks(request.user)

    context={
        'title':'PROFILE',
        'feeds':feeds,
        'followers':followers,
        'follower_usernames':follower_usernames,
        'followeds':followeds,
        'followed_usernames':followed_usernames,
        'bookmarks':bookmarks,
        'tag_list':tagged_feeds(request.user)
    }

    return render(request,'users/profile.html',context)


def dashboard(request,user_id):
    user=get_object_or_404(User,id=user_id)

    if user==request.user:
        return redirect(profile)

    else:
        user_feeds=Feed.objects.filter(creator=user).order_by('-timestamp').all()

        user_followers=Follow.objects.filter(followed_id=user).all()
        user_followeds=Follow.objects.filter(follower_id=user).all()

        followers=Follow.objects.filter(followed_id=request.user).all()
        followeds=Follow.objects.filter(follower_id=request.user).all()

        follower_usernames,followed_usernames=follow_usernames(followers,followeds)

        context={
            'title':user.username,
            'member':user,
            'feeds':user_feeds,
            'followers':user_followers,
            'followeds':user_followeds,
            'follower_usernames':follower_usernames,
            'followed_usernames':followed_usernames,
            'tag_list':tagged_feeds(user)
        }

        return render(request,'users/dashboard.html',context)



    



@login_required
def account(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'title':'ACCOUNT',
        'u_form':u_form,
        'p_form':p_form
    } 

    return render(request,'users/account.html',context)


@login_required
def follow(request,user_id):
    data=dict()
    f_user=get_object_or_404(User,id=user_id)
    if not is_following(request.user,f_user):
        f=Follow(follower_id=request.user,followed_id=f_user)
        f.save()
        data['follow_done']=True
        followers_count=Follow.objects.filter(followed_id=request.user).count()
        followeds_count=Follow.objects.filter(follower_id=request.user).count()
        data['followers_count']=followers_count
        data['followeds_count']=followeds_count
    else:
        data['follow_done']=False
    return JsonResponse(data)
    

@login_required
def unfollow(request,user_id):
    data=dict()
    f_user=get_object_or_404(User,id=user_id)
    if is_following(request.user,f_user):
        f=Follow.objects.filter(follower_id=request.user,followed_id=f_user)
        f.delete()
        data['unfollow_done']=True
        followers_count=Follow.objects.filter(followed_id=request.user).count()
        followeds_count=Follow.objects.filter(follower_id=request.user).count()
        data['followers_count']=followers_count
        data['followeds_count']=followeds_count
    else:
        data['unfollow_done']=False
    return JsonResponse(data)


@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            return redirect('change-password-done')
    else:
        form=PasswordChangeForm(request.user)         

    context={
        'form':form,
    }
    return render(request,'users/change_password.html',context)


@login_required
def change_password_done(request):
    form=PasswordChangeForm(request.user)         
    success_messege='Password has been successfully changed!'
    context={
        'form':form,
        'success_messege':success_messege
    }
    return render(request,'users/change_password.html',context)