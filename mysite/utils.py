from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, title):
        obj = get_object_or_404(self.model, title__iexact=title)
        return render(request, self.template, {self.model.__name__.lower(): obj})
