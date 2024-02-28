from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django_filters import FilterSet, ModelChoiceFilter
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm

# def welcome_page(request):
#     return HttpResponse("Hello. This is a welkome page.")

class PostList(ListView):
    model = Post
    ordering = 'date'
    template_name = 'post_list.html'
    context_object_name = 'postlist'
    paginate_by = 10

class CommentList(ListView):
    model = Comment
    ordering = 'date'
    template_name = 'comment_list.html'
    context_object_name = 'commentlist'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'postdetail'

class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    context_object_name = 'commentdetail'

class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    
    def form_valid(self, form):
        post = form.save(commit= False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

class CommentCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = CommentForm
    model = Comment
    template_name = 'comment_edit.html'

    def form_valid(self, form):
        comment = form.save(commit= False)
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class CommentUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = CommentForm
    model = Comment
    template_name = 'comment_edit.html'

class PostDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('postlist')


class CommentDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('commentlist')


class PostFilter(FilterSet):
    class Meta:
        model = Comment
        fields = [
            'post',       
        ]

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs),
        self.filters['post'].queryset = Post.objects.filter(author_id=kwargs['request'])

class UserPage(LoginRequiredMixin, ListView):
    model = Comment
    ordering = 'date'
    template_name = 'userpage.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        quesryset = Comment.objects.filter(post__author_id=self.request.user.id)
        self.filterset = PostFilter(self.request.GET, quesryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Comment.objects.none()

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context

