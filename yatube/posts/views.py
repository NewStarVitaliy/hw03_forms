from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings



from .forms import PostForm
from .models import Group, Post, User



def index(request):
    posts = Post.objects.all()
    title = 'Это главная страница проекта Yatube'
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts = Post.objects.filter(group=group).all()[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    posts_count = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'posts_count': posts_count,
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id) 
    context = {'post': post,
    }
    return render(request, 'posts/post_detail.html', context)



@login_required
def post_create(request):
    if request.method != 'POST':
        form = PostForm()
        return render(request, 'posts/create_post.html',
                      {'form': form})
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=post.author)
    return render(request, 'posts/create_post.html',
                  {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect('posts:post_detail', post_id=post_id)
    form = PostForm(
        request.POST or None,
        instance=post
    )
    is_edit = True
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('posts:post_detail', post.pk)
    context = {
        'post': post,
        'form': form,
        'is_edit': is_edit
    }
    return render(request, 'posts/create_post.html', context)