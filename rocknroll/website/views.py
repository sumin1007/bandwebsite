from django.shortcuts import render, redirect
from .models import Post
from .forms import CreateForm

# Create your views here.
def main(request):
    return render(request, 'website/main.html')

def layout(request):
    return render(request, 'website/layout.html')


def about(request):
    return render(request, 'website/about.html')


def community(request):
    posts = Post.objects
    return render(request, 'website/community.html', {'posts':posts})


def contact(request):
    return render(request, 'website/contact.html')


def music(request):
    return render(request, 'website/music.html')

def post(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('community')
    else:
        form = CreateForm()
        return render(request, 'website/post.html', {'form':form})