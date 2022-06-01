from django.db import models

# Create your models here.
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.conf import settings

# Create your models here.
class Post(models.Model):
    jobtype = [
        ("full-time", "full-time"),
        ("part-time", "part-time"),
    ]
    categories = [
        ("webdev", "Web Developers"),
        ("mobiledev", "Mobile Developers"),
        ("ui_ux", "UI/UX Designer"),
        ("mleng", "Machine Learning Engineer"),
        ("ds", "Data Scientist"),
        ("gamedev", "Game Developer"),
        ("isse", "Security Engineer"),
    ]
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)
    # company = models.CharField(max_length=70)
    salary = models.CharField(max_length=50, null=True)
    job_type = models.CharField(max_length=20, choices=jobtype)
    category = models.CharField(max_length=50, choices=categories)
    description = models.TextField()
    hours = models.CharField(max_length=50, null=True)

    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post-detail", kwargs={"pk": self.pk}
        )  # return full path as string
