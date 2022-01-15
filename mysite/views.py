from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Post, Quote
from .utils import *
from .forms import PostForm, QuoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

def post_list(request):
    search_query = request.GET.get('Search', '')

    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.order_by('-created_date')

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page', 3)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }

    return render(request, 'mysite/post_list.html', context=context)


def quote_list(request):
    quotes = Quote.objects.order_by('-created_date')

    paginator = Paginator(quotes, 3)

    page_number = request.GET.get('page', 3)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }

    return render(request, 'mysite/quote_list.html', context=context)


class QuoteDetail(ObjectDetailMixin, View):
    model = Quote
    template = 'mysite/quote_detail.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'mysite/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'mysite/post_create.html'
    raise_exception = True


class QuoteCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = QuoteForm
    template = 'mysite/quote_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'mysite/post_update.html'
    raise_exception = True


class QuoteUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Quote
    model_form = QuoteForm
    template = 'mysite/quote_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'mysite/post_delete.html'
    redirect_url = 'post_list'
    raise_exception = True


class QuoteDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Quote
    template = 'mysite/quote_delete.html'
    redirect_url = 'quote_list'
    raise_exception = True
