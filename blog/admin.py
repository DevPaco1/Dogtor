from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):

    fields= ["name"]


class BlogAdminArea(admin.AdminSite):
    """Blog admin panel"""

    site_header = "Blog Site Admin Area"

blog_admin_site = BlogAdminArea(name="BlogAdmin")

blog_admin_site.register(models.Post, PostAdmin)
admin.site.register(models.Post, PostAdmin)