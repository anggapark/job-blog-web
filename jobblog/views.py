from operator import truediv
from django.shortcuts import render
from .models import Post
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
def home(request):
    context = {"posts": Post.objects.all()}  # buat {{variabel}} template home html
    return render(request, "jobblog/index.html", context)


class PostListView(ListView):
    model = Post
    template_name = "jobblog/jobs.html"  # <apps>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-created_on"]  # latest post at the top


# access detail post
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        "title",
        "location",
        "job_type",
        "category",
        "salary",
        "description",
        "hours",
        "company",
        "website",
        "logo",
    ]


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # see if user pass test condition (update post)
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
