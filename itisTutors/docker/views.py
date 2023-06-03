from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import DockerPost
from tutors.models import Subject
from users.models import Course


def home(request):
    context = {
        'posts': DockerPost.objects.all()
    }
    return render(request, 'docker/home.html', context)


class SubjectListView(ListView):
    model = Subject
    template_name = 'docker/home.html'
    context_object_name = 'subjects'
    #ordering = ['-date_posted']
    paginate_by = 10

class SubjectPostListView(ListView):
    model = DockerPost
    template_name = 'docker/subject_posts.html'
    context_object_name = 'posts'
    paginate_by = 5


    def get_queryset(self):
        subj = get_object_or_404(Subject, pk=self.kwargs.get('pk'))
        posts = DockerPost.objects.filter(discipline=subj)
        return posts


class PostDetailView(DetailView):
    model = DockerPost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = DockerPost
    fields = ['title', 'postText','discipline','course']
    success_url = reverse_lazy('storage-home')
    def form_valid(self, form):
        #form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DockerPost
    fields = ['title', 'postText']
    success_url = reverse_lazy('storage-home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.Profile.tutorPermissions==True:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DockerPost
    success_url =  reverse_lazy('storage-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user.Profile.tutorPermissions==True:
            return True
        return False

