from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('register/',views.registration,name='registration'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('account/',views.account,name='account'),
    path('dashboard/<int:user_id>',views.dashboard,name='dashboard'),
    path('follow/<int:user_id>/',views.follow,name='follow'),
    path('unfollow/<int:user_id>/',views.unfollow,name='unfollow'),
    path('account/change_password/',views.change_password,name='change-password'),
    path('account/change_password_done/',views.change_password_done,name='change-password-done'),
]
