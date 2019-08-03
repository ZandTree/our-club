from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

MEMBERSHIP_CHOICES = (
    ('0','banned'),
    ('1','memeber'),
    ('2','moder'),
    ('3','admin'),

)

class Community(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(max_length=250,blank=True,default="")
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,
                                     through="CommunityMember")
    def __str__(self):
        return self._check_long_column_names
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'communities'
        # @property
        # def admin(self):
        #     return self.memberships.filter(role=3).value_list('user',flat=True)
        # @property
        # def moder(self):
        #     return self.memberships.filter(role=2).value_list('user')
        # @property
        # def good_members(self):
        #     return self.memberships.exclude(role=0)

class CommunityMember(models.Model):
    community = models.ForeignKey(Community,
                    on_delete=models.CASCADE,
                    related_name='memberships')
    user = models.ForeignKey(User,
                    on_delete=models.CASCADE,
                    related_name='communities')
    role = models.CharField(max_length = 5,choices=MEMBERSHIP_CHOICES,default= 1)
    def __str__(self):
        return "{} is {} in {}".format(self.user.username,self.role,self.community.name)
    class Meta:
        unique_together =('community','user')
