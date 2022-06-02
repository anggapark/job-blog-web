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
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
    ]
    categories = [
        ("Web Developers", "Web Developers"),
        ("Mobile Developers", "Mobile Developers"),
        ("UI/UX Designer", "UI/UX Designer"),
        ("Machine Learning Engineer", "Machine Learning Engineer"),
        ("Data Scientist", "Data Scientist"),
        ("Game Developer", "Game Developer"),
        ("Security Engineer", "Security Engineer"),
    ]
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50, blank=True)
    salary = models.CharField(max_length=50, blank=True)
    job_type = models.CharField(max_length=50, choices=jobtype)
    category = models.CharField(max_length=50, choices=categories)
    description = models.TextField()
    hours = models.CharField(max_length=50, blank=True)

    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    logo = models.ImageField(
        default="account.svg", upload_to="logo", blank=True, null=True
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         "post-detail", kwargs={"pk": self.pk}
    #     )  # return full path as string
