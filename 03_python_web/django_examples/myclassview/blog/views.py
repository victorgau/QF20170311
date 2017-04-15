from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

def create_post(request):
    if 'title' in request.GET and request.GET['title'] !='':
        title = request.GET['title']
        body = request.GET['body']
        Post.objects.create(title=title, body=body)
        return HttpResponseRedirect(reverse('post_list_view'))
    else:
        return render(request, 'blog/create_post.html', locals())

def create_postform(request):
    if request.POST:
        f = forms.PostForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            body = f.cleaned_data['body']

            p = Post.objects.create(title=title, body=body)
            return HttpResponseRedirect(reverse('post_list_view'))
    else:
        f = forms.PostForm()
    return render(request, 'blog/create_postform.html', locals())

def create_postmodelform(request):
    if request.POST:
        f = forms.PostModelForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            body = f.cleaned_data['body']

            p = Post.objects.create(title=title, body=body)
            return HttpResponseRedirect(reverse('post_list_view'))
    else:
        f = forms.PostModelForm()
    return render(request, 'blog/create_postmodelform.html', locals())
