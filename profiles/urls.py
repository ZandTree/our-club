from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('',views.UserProfile.as_view(),name='profile'),
]