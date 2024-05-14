from django.shortcuts import render
from .models import Post

# Create your views here.

def submitPost(request):
    if request.method == 'POST':
        post_text= request.POST.get('post')
        if post_text:
           Post.objects.create(text=post_text)
    posts = Post.objects.all()
    return render(request, 'submit.html', {'posts': posts})
