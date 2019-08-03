from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('detail-profile/<int:pk>/',views.UserProfile.as_view(),name='profile'),
    path('delete-profile/<int:pk>/',views.DeleteProfile.as_view(),name='del-profile'),
]
