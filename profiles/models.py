from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
import os

def make_avatar(instance,file):
    time = timezone.now().strftime('%Y-%m-%d')
    tail = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '.' + tail
    user_id = instance.user_id
    return os.path.join('avatars',str(user_id),time,file_name)

class Profile(models.Model):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120,default="")
    last_name = models.CharField(max_length=120,default="")
    age = models.SmallIntegerField(blank=True,null=True)
    location = models.CharField(max_length=120,default="")
    avatar = models.ImageField(blank=True,null=True,upload_to=make_avatar)


    def __str__(self):
        if self.first_name:
            return self.first_name
        elif self.first_name and self.last_name:
            return "{} {}".format(self.first_name,self.last_name)

        else:
            return "I'm Enigma"

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height >200 or img.width >200:
                output_size = (200,200)
                img.thumbnail(output_size)
                img.save(self.avatar.path)

    @property
    def get_avatar_path(self):
        if self.avatar:
            return "/media/{}".format(self.avatar)
        else:
            return '/static/img/icons/avatar.png/'
    # def get_absolute_url(self):
    #     return reverse('profiles:profile',kwargs={'pk':self.user_id})
    def get_absolute_url(self):
        return reverse('profiles:profile',kwargs={'pk':self.user_id})

def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
post_save.connect(create_profile,sender=User)
