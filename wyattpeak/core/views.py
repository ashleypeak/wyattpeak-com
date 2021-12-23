from django.http import HttpResponse
from django.shortcuts import render

from .models import PortfolioGroup, PortfolioItem, BlogPost


def index(request):
    context = {
        'portfolio_groups': PortfolioGroup.objects.all(),
        'portfolio_items': PortfolioItem.objects.all(),
        'blog_posts': BlogPost.objects.all(),
    }

    return render(request, 'core/index.html', context=context)


def portfolio(request, slug):
    try:
        context = {
            'item': PortfolioItem.objects.get(slug=slug)
        }
        return render(request, 'core/portfolio.html', context=context)
    except PortfolioItem.DoesNotExist:
        return HttpResponse('Portfolio item not found.')


def blog(request, slug):
    try:
        context = {
            'post': BlogPost.objects.get(slug=slug)
        }
        return render(request, 'core/blog.html', context=context)
    except BlogPost.DoesNotExist:
        return HttpResponse('Blog post not found.')
