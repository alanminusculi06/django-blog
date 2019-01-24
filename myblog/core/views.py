from django.shortcuts import render, redirect, reverse, HttpResponse
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, Contact


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def about(request):
    template_name = "about.html"
    return render(request, template_name)


def contact(request):
    template_name = "contact.html"
    context = {}
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            try:
                context['is_valid'] = True
                form.send_mail()
                form = Contact()
            except:
                context['is_valid'] = False
                context['erro'] = True           
    else:
        form = Contact()
    context['form'] = form
    return render(request, template_name, context)
