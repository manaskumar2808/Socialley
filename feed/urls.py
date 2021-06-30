from django.urls import path
from .views import FeedListView,FeedCreateView,FeedDetailView,FeedUpdateView,FeedDeleteView
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('feed/',FeedListView.as_view(),name='feed-home'),
    path('feed/<int:pk>/detail/',FeedDetailView.as_view(),name='feed-detail'),
    path('feed/create/',FeedCreateView.as_view(),name='feed-create'),
    path('feed/<int:pk>/update/',FeedUpdateView.as_view(),name='feed-update'),
    path('feed/<int:pk>/delete/',FeedDeleteView.as_view(),name='feed-delete'),
    path('feed/<int:feed_id>/like/',views.like,name='like'),
    path('feed/<int:feed_id>/unlike/',views.unlike,name='unlike'),
    path('feed/<int:feed_id>/comment/',views.comment,name='comment'),
    path('feed/<int:feed_id>/bookmark/',views.bookmark,name='bookmark'),
    path('feed/<int:feed_id>/unbookmark/',views.unbookmark,name='unbookmark'),
    path('feed/<int:feed_id>/comment/<int:comment_id>/like/',views.comment_like,name='comment_like'),
    path('feed/<int:feed_id>/comment/<int:comment_id>/unlike/',views.comment_unlike,name='comment_unlike'),
    path('feed/<int:feed_id>/tag/<int:user_id>/',views.tag,name='tag'),
    path('feed/<int:feed_id>/untag/<int:user_id>/',views.untag,name='untag'), 
]