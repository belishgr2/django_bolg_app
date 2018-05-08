from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    #  name = 'Django'
    # return HttpResponse('''<h1>Hello {Myname}</h1>'''.format(Myname=name))
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts': posts})