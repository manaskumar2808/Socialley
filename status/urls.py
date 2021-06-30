from django.urls import path
from .views import StatusCreateView,status_view

urlpatterns=[
    path('create/',StatusCreateView.as_view(),name='status-create'),
    path('view/<int:status_id>',status_view,name='status-view'),
]