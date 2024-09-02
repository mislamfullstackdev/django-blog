from .models import Post

def latest_posts(request):
    latest_posts = Post.objects.order_by('-date_posted')[:5]
    return {'latest_posts': latest_posts}