from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.db.models import Q
from django.forms import modelformset_factory
from .models import Feed,Gallery,Like,Comment,Bookmark,Tag
from .forms import GalleryForm
from users.models import Follow
from users.utils import follow_usernames,user_bookmarks,follow_status
from .utils import has_liked,feed_comments,has_liked_comments,tagged_users
from status.models import Status
from datetime import datetime,timedelta


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('feed-home')

    else:
        return redirect('logout')


class FeedListView(ListView):
    model=Feed
    template_name='feed/home.html'
    context_object_name='feeds'
    ordering=['-timestamp']

    status_time_limit=24    

    def get_context_data(self,**kwargs):
        context=super(FeedListView,self).get_context_data(**kwargs)
        context['title']='HOME'
        context['suggestions']=User.objects.all()[:5]
        context['members']=User.objects.all()
        context['liked_feeds']=has_liked(self.request.user)
        context['liked_comments']=has_liked_comments(self.request.user)
        context['bookmarked_feeds']=user_bookmarks(self.request.user)
        context['follower_usernames'],context['followed_usernames']=follow_status(self.request.user)
        context['statuses']=Status.objects.filter( Q(timestamp__range=(datetime.utcnow()-timedelta(hours=self.status_time_limit),datetime.utcnow())) & ( Q(setter__in=context['followed_usernames']) | Q(setter=self.request.user) ) ).all().order_by('-timestamp')
        return context

    def get_queryset(self):
        follower_usernames,followed_usernames=follow_status(self.request.user)
        return Feed.objects.filter(Q(creator__in=followed_usernames) | Q(creator=self.request.user)).order_by('-timestamp').all()


def like(request,feed_id):
    data=dict()
    feed=get_object_or_404(Feed,id=feed_id)
    like=Like(feed_id=feed,liker_id=request.user)
    like.save()
    feed.likes+=1
    feed.save()

    data['count']=feed.likes

    return JsonResponse(data)


def unlike(request,feed_id):
    data=dict()
    feed=get_object_or_404(Feed,id=feed_id)
    like=Like.objects.filter(feed_id=feed,liker_id=request.user)
    like.delete()
    feed.likes-=1
    feed.save()

    data['count']=feed.likes

    return JsonResponse(data)

def comment_like(request,feed_id,comment_id):
    data=dict()
    comment=get_object_or_404(Comment,id=comment_id)
    like=Like(comment_id=comment,liker_id=request.user)
    like.save()
    comment.likes+=1
    comment.save()

    data['count']=comment.likes
    print(data['count'])

    return JsonResponse(data)

def comment_unlike(request,feed_id,comment_id):
    data=dict()
    comment=get_object_or_404(Comment,id=comment_id)
    like=Like.objects.filter(comment_id=comment,liker_id=request.user)
    like.delete()
    comment.likes-=1
    comment.save()

    data['count']=comment.likes
    print(data['count'])

    return JsonResponse(data)


def bookmark(request,feed_id):
    data=dict()
    feed=get_object_or_404(Feed,id=feed_id)
    bookmark=Bookmark(user_id=request.user,feed_id=feed)
    bookmark.save()
    data['bookmarked']=True

    return JsonResponse(data)



def unbookmark(request,feed_id):
    data=dict()
    feed=get_object_or_404(Feed,id=feed_id)
    bookmark=Bookmark.objects.filter(user_id=request.user,feed_id=feed)
    bookmark.delete()
    data['unbookmarked']=True

    return JsonResponse(data)



def comment(request,feed_id):
    if request.method=='POST':
        feed=get_object_or_404(Feed,id=feed_id)
        comment=Comment(comment_text=request.POST.get('commentText'),feed_id=feed,commentor_id=request.user)
        comment.save()
        feed.comments+=1
        feed.save()

        data=dict()
        data['commentor_image_url']=comment.commentor_id.profile.image.url
        data['commentor_username']=comment.commentor_id.username
        data['comment_text']=comment.comment_text 

        return JsonResponse(data)
    return redirect(DetailView,request=request,pk=feed_id)



class FeedDetailView(DetailView):
    model=Feed
    template_name='feed/feed_view.html'
    context_object_name='feed'

    def get_context_data(self,**kwargs):
        context=super(FeedDetailView,self).get_context_data(**kwargs)

        context['title']='DETAIL'
        context['feeds']=Feed.objects.filter(creator=context['object'].creator).exclude(id=context['object'].id).order_by('-timestamp')
        context['liked_feeds']=has_liked(self.request.user)
        context['liked_comments']=has_liked_comments(self.request.user)
        context['feed_comments']=feed_comments(context['object'])
        context['bookmarked_feeds']=user_bookmarks(self.request.user)
        context['followers']=Follow.objects.filter(followed_id=self.request.user)
        context['followeds']=Follow.objects.filter(follower_id=self.request.user)
        context['tagged_usernames']=tagged_users(self.request.user,context['object'])

        return context
    



class FeedCreateView(LoginRequiredMixin,CreateView):
    model=Feed
    fields=['title','image','video','description']
    extra_context={
        'title':'CREATE FEED'
    }

    def get_context_data(self,**kwargs):
        context=super(FeedCreateView,self).get_context_data(**kwargs)
        context['followers']=Follow.objects.filter(followed_id=self.request.user)
        context['followeds']=Follow.objects.filter(follower_id=self.request.user)
        context['g_form']=GalleryForm()
        return context

    
    def form_valid(self,form):
        form.instance.creator=self.request.user

        validity=super().form_valid(form)

        gallery_form=GalleryForm(self.request.POST,self.request.FILES)
        images=self.request.FILES.getlist('gallery')
        print('creating gallery')
        if validity and gallery_form.is_valid():
            feed_id=form.instance
            for image in images:
                g=Gallery(feed_id=feed_id,gallery=image)
                g.save()

        return validity


class FeedUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Feed
    fields=['title','image','video','description']
    extra_context={
        'title':'UPDATE FEED'
    }

    def get_context_data(self,**kwargs):
        context=super(FeedUpdateView,self).get_context_data(**kwargs)
        context['followers']=Follow.objects.filter(followed_id=self.request.user)
        context['followeds']=Follow.objects.filter(follower_id=self.request.user)
        context['g_form']=GalleryForm()
        return context


    def form_valid(self,form):
        form.instance.creator=self.request.user

        gallery_form=GalleryForm(self.request.POST,self.request.FILES)
        images=self.request.FILES.getlist('gallery')
        if gallery_form.is_valid():
            feed_id=form.instance
            for image in images:
                g=Gallery(feed_id=feed_id,gallery=image)
                g.save()
            
        return super().form_valid(form)

    def test_func(self):
        feed=self.get_object()
        if feed.creator==self.request.user:
            return True
        return False


def tag(request,feed_id,user_id):
    data=dict()
    feed=get_object_or_404(Feed,id=feed_id)
    tagged_user=get_object_or_404(User,id=user_id)
    t=Tag(tagger_id=request.user,tagged_id=tagged_user,feed_id=feed)
    t.save()
    data['tag_successful']=True
    return JsonResponse(data)


def untag(request,feed_id,user_id):
    data=dict()
    feed=get_object_or_404(Feed,id=feed_id)
    tagged_user=get_object_or_404(User,id=user_id)
    t=Tag.objects.filter(tagger_id=request.user,tagged_id=tagged_user,feed_id=feed)
    t.delete()
    data['untag_successful']=True
    return JsonResponse(data)


class FeedDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Feed
    success_url='/'
    template_name='feed/feed_delete.html'
    context_object_name='feed'
    extra_context={
        'title':'DELETE FEED'
    }

    def test_func(self):
        feed=self.get_object()
        if feed.creator==self.request.user:
            return True
        return False