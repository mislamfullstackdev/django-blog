from django.shortcuts import render
from django.http import HttpResponse


# dummy 
posts = [
    {
        'author': 'Kamrul Islam',
        'title' : 'Blog Post 1',
        'content' : 'Blog post body',
        'date_posted': 'August 8, 2024'
    },
    {
        'author': 'John Dou',
        'title' : 'Blog Post 2',
        'content' : 'Blog post2 body',
        'date_posted': 'August 9, 2024'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
