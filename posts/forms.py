from .models import Post
from communities.models import Community
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('message',"community")
    def __init__(self,*args,**kwargs):
        # get  user from kwargs # but not like this user = self.request.user
        user = kwargs.pop("user",None)
        super().__init__(*args,**kwargs)
        if user is not None:
            self.fields['community'].queryset = Community.objects.filter(
                        pk__in=user.communities.values_list("community__pk")
                    )
