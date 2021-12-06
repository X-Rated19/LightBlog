from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Post, Quote
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import PostForm, QuoteForm


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'mysite/post_list.html', {'posts': posts})


def quote_list(request):
    quotes = Quote.objects.order_by('-created_date')
    return render(request, 'mysite/quote_list.html', {'quotes': quotes})


class QuoteDetail(ObjectDetailMixin, View):
    model = Quote
    template = 'mysite/quote_detail.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'mysite/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'mysite/post_create.html'


class QuoteCreate(ObjectCreateMixin, View):
    model_form = QuoteForm
    template = 'mysite/quote_create.html'