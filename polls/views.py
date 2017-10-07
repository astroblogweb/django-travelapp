from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Polls,PollsForm

def all_polls(request):
    #return HttpResponse("at polls index")
    polls=Polls.objects.all()
    #print(polls)
    return render(request,"polls_list.html",{"polls":polls})

def polls_detail(request,pk):
    polls=get_object_or_404(Polls,pk=pk)
    print(polls)
    return render(request,"polls_detail.html",{"polls":polls})

def polls_vote(request,pk):
    print("voting")

    question=get_object_or_404(Polls,pk=pk)
    print(request.POST)
    choice_pk_id=request.POST.get("choice")
    print(choice_pk_id)
    #print(question)
    #choice_vote=question.choice_set.get(pk=request.POST.["choice"])
    #choice_vote=question.choice_set.get(pk=request.POST.get('choice',1))
    choice_vote=question.choice_set.get(choice_pk_id)
    #print("form:",form)
    print("choice vote:", choice_vote)
    choice_vote.votes+=1
    choice_vote.save()

    polls=Polls.objects.get(pk=pk)
    return render(request,"polls_detail.html",{"polls":polls})




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))