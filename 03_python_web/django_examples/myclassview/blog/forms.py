from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(label='標題', max_length=255)
    body = forms.CharField(label='內容', max_length=255, widget=forms.Textarea)

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
