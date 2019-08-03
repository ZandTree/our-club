from django.urls import path,re_path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.AllPosts.as_view(),name='all'),
    path('create-post',views.CreatePost.as_view(),name='create-post'),
    re_path(r'^detail-post/(?P<username>[-\w]+)/$',views.SinglePost.as_view(),name='single-post'),
    # posts only of particular user
    re_path(r'^user-posts/(?P<member>[-\w]+)/$',views.UserPost.as_view(),name='user-post'),

]
