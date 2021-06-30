from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.db.models import Q
from .models import Status
from .forms import StatusForm
from users.utils import follow_status
from datetime import datetime,timedelta


# Create your views here.

class StatusCreateView(LoginRequiredMixin,CreateView):
    model=Status
    fields=['caption','image','video']
    template_name='status/create_status.html'

    def get_context_data(self,**kwargs):
        context=super(StatusCreateView,self).get_context_data(**kwargs)
        context['title']='STATUS CREATE'
        return context

    def form_valid(self,form):
        form.instance.setter=self.request.user
        if form.is_valid():
            form.save()
        
        return super().form_valid(form)
        

def status_view(request,status_id):
    status_time_limit=24
    set_time=datetime.utcnow()-timedelta(hours=status_time_limit)
    unset_time=datetime.utcnow()



    follower_usernames,followed_usernames=follow_status(request.user)
    statuses=Status.objects.filter( Q(timestamp__range=(set_time,unset_time)) & (Q(setter__in=followed_usernames) | Q(setter=request.user.id)) ).all().order_by('-timestamp')
    current_status=get_object_or_404(Status,id=status_id)
    prev_status=Status.objects.filter( Q(timestamp__gt=current_status.timestamp) & ( Q(setter__in=followed_usernames) | Q(setter=request.user.id) ) ).order_by('timestamp').first()
    next_status=Status.objects.filter( Q(timestamp__lt=current_status.timestamp) & ( Q(setter__in=followed_usernames) | Q(setter=request.user.id) ) ).order_by('-timestamp').first()
    context={
        'title':'STATUS VIEW',
        'statuses':statuses,
        'current_status':current_status,
        'prev_status':prev_status,
        'next_status':next_status,
    }

    return render(request,'status/view_status.html',context)