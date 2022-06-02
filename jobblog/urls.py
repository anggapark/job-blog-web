from winreg import DeleteValue
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostHome,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from django.conf.urls.static import static
from django.conf import settings

app_name = "jobblog"
urlpatterns = [
    path("", PostHome.as_view(), name="home"),
    path("post/job/", PostListView.as_view(), name="jobs"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/<slug:slug>/", PostDetailView.as_view(), name="post"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
