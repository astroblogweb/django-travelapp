from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .models import UserForm


class UserFormView(View):
    form_class=UserForm
    template_name="registration.html"
    def get(self, request):
        form=self.form_class(None)
        print("get")
        return render(request,self.template_name,{'form':form})


    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user.set_password(password)
            user.save()
            print("user-registered")
            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('homepage')
        return render(request,self.template_name,{'form':form})

