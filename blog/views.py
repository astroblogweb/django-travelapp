from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
#from .forms import BlogForm

from .models import Blog,BlogForm

def blog_new(request):
    if request.method == 'GET':
        form = BlogForm()
        print("request is get")
    else:
        form = BlogForm(request.POST)
        print("request is post")
        if form.is_valid():
            blog=form.save(commit=False)
            blog.title = form.cleaned_data['title']
            blog.content = form.cleaned_data['content']
            blog.save()
            print("going to return to success.. and then to redirect to blog detail")
            return HttpResponse("successful Http-Response")
#    return HttpResponse("Un--successful Http-Response")


def success(request):
#    return HttpResponse('Success! Thank you for your message.')
    return render_to_response("success.html")


def blog_list(request):
    print("inside blog list")
    #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    blogs=Blog.objects.all()
    print(blogs)
    #return HttpResponse(blogs)
    return render(request,"blog_list.html",{"blogs":blogs})

def blog_detail(request,pk):
    print("inside blog detail")
    #return HttpResponse("blog detail..")
    blog=get_object_or_404(Blog,pk=pk)
    return render(request,"blog_detail.html",{"blog":blog})
