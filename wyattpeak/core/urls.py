from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<slug:slug>/', views.portfolio, name='portfolio'),
    path('code-samples/<slug:slug>/', views.code_sample, name='code_samples'),
    path('blog/<slug:slug>/', views.blog, name='blog'),
]
