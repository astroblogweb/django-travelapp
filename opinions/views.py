from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Opinions
from django.views import generic

class Opinions_List(generic.ListView):
    template_name="opinions_list.html"
    context_object_name="opinions"
    def get_queryset(self):
        return Opinions.objects.order_by('pub_date')


class Opinions_Detail(generic.DetailView):
    model=Opinions
    template_name="opinions_detail.html"
    # note : context object passed would be 'model_name' in small letters.
    # accordingly make the html page



class Opinions_Result(generic.DetailView):
    model=Opinions
    template_name="opinions_result.html"


def opinions_vote(request,pk):
    print("voting")
    if request.method=="POST":
        opinion=get_object_or_404(Opinions,pk=pk)
        # print("request POST:",request.POST)
        # choice_pk_id=request.POST.get('choice')
        # print("choice_pk_id",choice_pk_id)
        choice_vote=opinion.choice_set.get(pk=request.POST['choice'])
        #print("form:",form)
        # print("choice vote:", choice_vote)
        choice_vote.votes+=1
        choice_vote.save()
        opinion=Opinions.objects.get(pk=pk)
        return render(request,"opinions_result.html",{"opinion":opinion})
    else:
        print("request is get")
        opinion=Opinions.objects.get(pk=pk)
        return render(request,"opinions_vote.html",{"opinion":opinion})
    opinion=Opinions.objects.get(pk=pk)
    return render(request,"opinions_vote.html",{"opinion":opinion})


