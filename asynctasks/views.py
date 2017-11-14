from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import DataGen
from .forms import GenerateDataGenForm
from .tasks import create_data_gen

class GenerateRandomUserView(FormView):
    template_name = "async_tasks.html"
    form_class = GenerateDataGenForm
    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        print("total:",total)
        create_data_gen.delay(total)
        messages.success(self.request,
            'Generating your random users! Wait a moment and refresh this page.')
        return redirect('asynctasks:taskdone')

class TaskdoneListView(ListView):
    template_name="task_done.html"
    context_object_name="data_gen"
    def get_queryset(self):
        return DataGen.objects.all()
