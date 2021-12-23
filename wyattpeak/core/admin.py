from django.contrib import admin

from .models import PortfolioGroup, PortfolioItem, BlogPost, Image, Tag


@admin.register(PortfolioGroup)
class PortfolioGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('path', 'alt_text')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
