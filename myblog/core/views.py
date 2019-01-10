from django.shortcuts import render, HttpResponse

def post_list(request):
    return render(request, 'post_list.html', {})
