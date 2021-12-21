from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def portfolio(request, slug):
    return render(request, 'core/portfolio.html', {'title': 'Occam'})


def blog(request, slug):
    return render(request, 'core/blog.html', {'title': 'Blog post'})
