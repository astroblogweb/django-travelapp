from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import ContactForm


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            print("going to return to success..")
#            return redirect('success')
#            return HttpResponse("successful Http-Response")
            return render_to_response("success.html")
#            render(request,"success.html",{'success_msg':"Successfulllll"})
    return render(request, "email.html", {'form': form})


def success(request):
#    return HttpResponse('Success! Thank you for your message.')
    return render_to_response("success.html")


