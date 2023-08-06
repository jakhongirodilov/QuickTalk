from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import TemplateView
from accounts.models import CustomUser, Profile
from .forms import PostForm, CommentForm
from .models import Comment, Post
from django.contrib.auth.decorators import login_required


@login_required
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post', args=[str(pk)]))


def home_page(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    form = PostForm()

    return render(request, 'index.html', {'form': form, })


@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})


@login_required
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        print(current_user_profile)
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    followers_count = profile.follows.count()

    context = {
        'profile': profile,
        'followers_count':followers_count,
    }
    return render(request, 'profile.html', context)


@login_required
def post(request, pk):
    post = Post.objects.get(pk=pk)
    total_likes = post.total_likes()

    liked = False
    if post.likes.filter(id = request.user.id).exists():
        liked = True

    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post', pk=post.pk)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'total_likes': total_likes,
        'liked': liked
    }
    return render(request, 'post1.html', context)



