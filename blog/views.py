from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .modelForms import PostModelForm, PostForm
# Create your views here.
#글 리스트
def post_list(request):
    #  name = 'Django'
    # return HttpResponse('''<h1>Hello {Myname}</h1>'''.format(Myname=name))
    #posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts=Post.objects.all()
    return render(request,'blog/post_list.html',{'posts': posts})
#글 상세
def post_detail(request,pk):
    post= get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})
#글 등록 modelForm
def post_new(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else :
        form = PostModelForm()
        print(form)
    return render(request,'blog/post_edit.html',{'form':form})

#글 등록 Form 사용
def post_new_form(request) :
    if request.method == "POST" :
        form = PostForm(request.POST)
        #print(form)
        if form.is_valid():
            # 검증에성공한값들을dict타입으로제공받아서이값을DB에저장하기
            form.cleaned_data
            #방법 1 POST 객체 생성 save() 호출
            # post = Post(author=request.user,title=form.cleaned_data['title'],text=form.cleaned_data['text'],published_date=timezone.now())
            # post.save()
            #방법 2
            post = Post.objects.create(author=request.user,title=form.cleaned_data['title'],text=form.cleaned_data['text'],published_date=timezone.now())
            return redirect('post_detail',pk=post.pk)
        else:
            form.errors
    else :
        form = PostForm()
    return render(request,'blog/post_form.html',{'form':form})


def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST" :
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect("post_detail",pk=post.pk)
    else :
        form = PostModelForm(instance=post)
    return render(request,"blog/post_edit.html",{"form" : form})