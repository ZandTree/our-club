from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# from communites.models import Community



class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(max_length=256)
    #message_html = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True,null=True)
    # community = models.ForeignKey(Community,null=True,blank=True,
    #                             related_name='posts',on_delete=models.SET_NULL
    #                             )

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        #self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs = {
                'username':self.user.username,
                'pk':self.pk
                })
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user","message"]          
