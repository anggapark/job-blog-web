from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_on", "updated_on", "author")
    list_filter = ("created_on", "updated_on")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
