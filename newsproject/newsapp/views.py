from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class News(ListView):
    model = Post
    ordering = '-time'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = Post.objects.all()
        context['amount'] = 0
        for i in a:
            if i.type == 0:
                context['amount'] += 1
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'



