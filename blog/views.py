from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Post, Comment



def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})



@login_required
def create_post(request):
    if request.method == 'POST':
        Post.objects.create(
            author=request.user,
            content=request.POST['content']
        )
    return redirect('home')



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST" and request.user.is_authenticated:
        text = request.POST.get("text")
        if text:
            Comment.objects.create(
                post=post,
                author=request.user,
                text=text
            )
            return redirect("post_detail", post_id=post.id)

    return render(request, "blog/post_detail.html", {"post": post})



def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
