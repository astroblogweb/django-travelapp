from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse
from .models import Resume, ResumeForm
from django.views import generic

def resume(request):
    return HttpResponse("resume.")


def rate(request):
    if request.is_ajax():
        if request.method == 'GET':
            message = "fail"
        elif request.method == 'POST':
            user = request.POST.get('user')
            rating = request.POST.get('rating')
            this_id = request.POST.get('id')
            message = str(user) + " "+ str(rating) + " " +str(id)
    else:
        message = "No XHR"
    # do something
    return HttpResponse(message)



def edit_resume(request,pk):
    resume=get_object_or_404(Resume, pk=pk)
    if request.method=="POST":
        form=ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume=form.save(commit=False)
            resume.save()
    else:
        print("edit resume:GET")
        form=ResumeForm(instance=resume)
        return render(request,"edit_resume.html",{'form':form})
    return render(request,"detail_resume.html",{'resume':resume})


def newresume(request):
    if request.method=="POST":
        print("new resume Post")
        form=ResumeForm(request.POST)
        if form.is_valid():
            resume=form.save(commit=False)
            resume.firstname=form.cleaned_data['firstname']
            resume.lastname=form.cleaned_data['lastname']
            resume.dateofbirth=form.cleaned_data['dateofbirth']
            resume.style=form.cleaned_data['style']
            resume.save()
            print("new resume saved")
            ####return render(request,"detail_resume.html",{'listresume':Resume.objects.all()})
        return render(request,"list_resume.html",{'listresume':Resume.objects.all()})
    else:
        print("new resume Get")
        resumeform=ResumeForm()
    return render(request,"new_resume_form.html",{'resumeform':resumeform})


class ListResume(generic.ListView):
    template_name="list_resume.html"
    context_object_name="listresume"
    def get_queryset(self):
        return Resume.objects.order_by('-dateofbirth')

class DetailResume(generic.DetailView):
    model=Resume
    template_name="detail_resume.html"