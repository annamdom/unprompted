from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment, Profile



# PUBLIC LANDING PAGE

def landing(request):
    return render(request, "blog/landing.html")



# FEED (LOGIN REQUIRED)

@login_required
def feed(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/home.html", {"posts": posts})



# CREATE POST

@login_required
def create_post(request):
    if request.method == "POST":
        Post.objects.create(
            author=request.user,
            content=request.POST.get("content"),
        )
    return redirect("feed")



# POST DETAIL + COMMENTS

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Comment.objects.create(
                post=post,
                author=request.user,
                text=text,
            )
            return redirect("post_detail", post_id=post.id)

    return render(request, "blog/post_detail.html", {"post": post})



# SIGN UP

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})



# MY PROFILE

@login_required
def my_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    posts = Post.objects.filter(author=request.user).order_by("-created_at")

    return render(request, "blog/profile.html", {
        "profile": profile,
        "posts": posts,
        "is_owner": True,
    })



# EDIT PROFILE

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.bio = request.POST.get("bio", "")
        profile.user.first_name = request.POST.get("name", "")

        if "avatar" in request.FILES:
            profile.avatar = request.FILES["avatar"]

        profile.user.save()
        profile.save()
        return redirect("profile")

    return render(request, "blog/edit_profile.html", {"profile": profile})



# USER LIST


@login_required
def user_list(request):
    query = request.GET.get("q", "")
    profiles = Profile.objects.select_related("user")

    if query:
        profiles = profiles.filter(
            user__username__icontains=query
        )

    return render(request, "blog/users.html", {
        "profiles": profiles,
        "query": query,
    })




# PUBLIC USER PROFILE

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    posts = Post.objects.filter(author=user).order_by("-created_at")

    return render(request, "blog/profile.html", {
        "profile": profile,
        "posts": posts,
        "is_owner": False,
    })



# SEARCH POSTS

@login_required
def search(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(
        content__icontains=query
    ).order_by("-created_at")

    return render(request, "blog/home.html", {
        "posts": posts,
        "search_query": query,
    })

# EDIT POST

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == "POST":
        post.content = request.POST.get("content")
        post.save()
        return redirect("post_detail", post_id=post.id)

    return render(request, "blog/edit_post.html", {"post": post})



# DELETE POST

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == "POST":
        post.delete()
        return redirect("feed")

    return render(request, "blog/delete_confirm.html", {
        "object": post,
        "type": "post",
    })



# DELETE COMMENT

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_id = comment.post.id

    if request.method == "POST":
        comment.delete()
        return redirect("post_detail", post_id=post_id)

    return render(request, "blog/delete_confirm.html", {
        "object": comment,
        "type": "comment",
    })

#DELETE PROFILE

@login_required
def delete_profile(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("landing")