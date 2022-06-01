from winreg import DeleteValue
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from django.conf.urls.static import static
from django.conf import settings

app_name = "jobblog"
urlpatterns = [
    path("", views.home, name="home"),
    path("post/job", PostListView.as_view(), name="jobs"),
    path(
        "post/<int:pk>/", PostDetailView.as_view(), name="post-detail"
    ),  # select spesific post
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
