from msilib.schema import ListView,CreateView,DetailView,UpdateView
from django.shortcuts import render
from Daton1.blog.models import Post


class PostListView(ListView):
    model=Post


class PostCreatView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model=Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

