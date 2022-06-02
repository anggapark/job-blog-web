from operator import truediv
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.mixins import (
    LoginRequiredMixin,  # redirect unlogged user to login page when create post
    UserPassesTestMixin,  # to make sure only the writer can update the post
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.
class PostHome(ListView):
    model = Post
    template_name = "jobblog/index.html"
    context_object_name = "posts"
    ordering = ["-created_on"]

    def get_queryset(self):
        return Post.objects.filter().order_by("-created_on")[0:3]


class PostListView(ListView):
    model = Post
    template_name = "jobblog/jobs.html"  # <apps>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-created_on"]  # latest post at the top


# access detail post
class PostDetailView(DetailView):
    model = Post
    template_name = "jobblog/job-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]

        post = get_object_or_404(Post, pk=pk, slug=slug)
        context["post"] = post
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "jobblog/post_form.html"
    fields = [
        "title",
        "salary",
        "job_type",
        "category",
        "description",
        "hours",
        "company_name",
        "location",
        "website",
        "logo",
    ]

    def get_success_url(self):
        messages.success(self.request, "Your post has been created successfully.")
        return reverse_lazy("jobblog:jobs")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data["title"])
        obj.save()
        # form.save_m2m()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        "title",
        "location",
        "job_type",
        "category",
        "salary",
        "description",
        "hours",
        "company_name",
        "website",
        "logo",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # if user pass test condition (update post)
    def test_func(self):
        post = self.get_object()
        # check if the user is the author of the post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"  # Provide a success_url.

    # see if user pass test condition (update post)
    def test_func(self):
        post = self.get_object()
        # check if the user is the author of the post
        if self.request.user == post.author:
            return True
        return False
