from django.shortcuts import render
from django.views.generic import DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.urls import reverse_lazy


#
# class RestrictToUserList:
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(user=self.request.user)


class UserProfile(LoginRequiredMixin,DetailView):
    model = Profile

class DeleteProfile(LoginRequiredMixin,DeleteView):
    model = Profile
    success_url = reverse_lazy('posts:all')
