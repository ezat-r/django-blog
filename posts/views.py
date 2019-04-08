from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

def getPosts(request):
    """
    Create a view that will return a list of
    Posts that were published prior to now
    """

    posts = Post.objects.filter(publishedDate__lte=timezone.now()
        ).order_by('-publishedDate')

    return render(request, "blog-posts.html", {"posts": posts})

def postDetail(request, pk):
    """
    create a view that returns a single
    Post object based on the ID (pk) and
    render it to the 'post-details.html'
    template. Or return a 404 error if not
    found.
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    return render(request, "post-detail.html", {"post": post})

def createOrEditPost(request, pk=None):
    """
    create a view that allows us to create
    or edit a post depending if the post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            return redirect(postDetail, post.pk)
    
    else:
        form = BlogPostForm(instance=post)

    return render(request, "blog-post-form.html", {"form": form})