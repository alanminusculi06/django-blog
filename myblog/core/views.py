from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})