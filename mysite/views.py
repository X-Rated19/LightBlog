from django.shortcuts import render
from django.utils import timezone
from .models import Post, Quote


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mysite/post_list.html', {'posts': posts})

def quote_list(request):
    quotes = Quote.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mysite/quote_list.html', {'quotes': quotes})

def quote_detail(request, title):
    quote = Quote.objects.get(title__iexact=title)
    return render(request, 'mysite/quote_detail.html', {'quote': quote})

def post_detail(request, title):
    post = Post.objects.get(title__iexact=title)
    return render(request, 'mysite/post_detail.html', {'post': post})

