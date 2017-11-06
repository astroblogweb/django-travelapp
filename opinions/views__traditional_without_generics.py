from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Opinions


def all_opinions(request):
    opinions=Opinions.objects.order_by('pub_date')
    template=loader.get_template("opinions_list.html")
    context={"opinions":opinions}
    return HttpResponse(template.render(context, request))
    #return render(request,"opinions_list.html",context)

def opinions_detail(request,pk):
    opinion=get_object_or_404(Opinions,pk=pk)
    # try:
    #     question = Opinions.objects.get(pk=pk)
    # except Opinions.DoesNotExist:
    #     raise Http404("Opinions does not exist")
    print(opinion)
    return render(request,"opinions_detail.html",{"opinion":opinion})


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



def opinions_result(request, pk):
    print("results")
    opinion=Opinions.objects.get(pk=pk)
    return render(request,"opinions_result.html",{"opinion":opinion})

