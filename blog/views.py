from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
#from .forms import BlogForm
from django.utils import timezone
from .models import Blog,BlogForm
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

def blog_new(request):
    # form=BlogForm()
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
            #return redirect(reverse_lazy("blog_detail"),pk=blog.pk)
            # needs relative path for .html, so give url-name
            return render(request,"blog_detail.html",{"blog":blog})
    return render(request,"blog_new.html",{"form":form})


def blog_edit(request,pk):
    print("inside blog_edit")
    blog=get_object_or_404(Blog,pk=pk)
    if request.method == "POST":

        form = BlogForm(request.POST, instance=blog)
        print("request is post")


        if form.is_valid():
            blog=form.save(commit=False)
            #blog.title = form.cleaned_data['title'
            #blog.content = form.cleaned_data['content']
            blog.pub_date = timezone.now()
            blog.save()
            #return redirect("blog/blog_detail",pk=blog.pk)
            # return redirect(reverse_lazy("blog_detail"),pk=blog.pk)
            # needs relative path for .html, so give url-name
            return render(request,"blog_detail.html",{"blog":blog})


        #return HttpResponse("edited")
    else:
        form = BlogForm(instance=blog)
        print("request is get")
        return render(request, "blog_edit.html", {'form': form})
    #return render(request,"blog_detail.html",{"blog":blog})
    return HttpResponse("end")


def success(request):
#    return HttpResponse('Success! Thank you for your message.')
    return render_to_response("success.html")


def blog_list(request):
    print("inside blog list")
    blogs=Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    #blogs=Blog.objects.all()
    print(blogs)
    #return HttpResponse(blogs)
    return render(request,"blog_list.html",{"blogs":blogs})

def blog_detail(request,pk):
    print("inside blog detail")
    #return HttpResponse("blog detail..")
    blog=get_object_or_404(Blog,pk=pk)
    return render(request,"blog_detail.html",{"blog":blog})


# {% static 'css/blog.css' %}
