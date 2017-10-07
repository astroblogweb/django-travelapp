from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
#from .forms import BlogForm

from .models import Blog,BlogForm

def blog_new(request,pk):
    if request.method == 'GET':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.title = form.cleaned_data['title']
            blog.content = form.cleaned_data['content']
            blog.created_date = form.cleaned_data['created_date']
            blog.pub_date = form.cleaned_data['pub_date']
            blog.save()
            # try:
            #     send_mail(subject, message, from_email, ['admin@example.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            print("going to return to success.. and then to redirect to blog detail")
#            return redirect('success')
            return HttpResponse("successful Http-Response")
            #return render_to_response("success.html")
#            render(request,"success.html",{'success_msg':"Successfulllll"})
    #return render(request, "email.html", {'form': form})
    return HttpResponse("Un--successful Http-Response")


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
