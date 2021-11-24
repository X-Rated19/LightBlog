from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Post, Quote
from .utils import ObjectDetailMixin


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mysite/post_list.html', {'posts': posts})

def quote_list(request):
    quotes = Quote.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mysite/quote_list.html', {'quotes': quotes})

class QuoteDetail(ObjectDetailMixin, View):
    model = Quote
    template = 'mysite/quote_detail.html'
    # def get(self, request, title):
    #     quote = get_object_or_404(Quote, title__iexact=title)
    #     return render(request, 'mysite/quote_detail.html', {'quote': quote})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'mysite/post_detail.html'
    # def get(self, request, title):
    #     post = get_object_or_404(Post, title__iexact=title)
    #     return render(request, 'mysite/post_detail.html', {'post': post})
