from django.db import models
from django.forms import ModelForm
from django import forms
from django.conf import settings
#from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Blogpost(models.Model):
    user = models.ForeignKey(User, default=1, null=True,  on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null= True, blank=True)

    def get_absolute_url(self):
        return f"/blog"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"



class Blogpostuser(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title','slug','content']

   


