from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect


from .forms import FeedbackForm
from posts.models import Post#, Tag


def feedback(request):
    # queryset = Post.objects.active()
    form = FeedbackForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            # form.save()
            form_fullname = form.cleaned_data.get("fullname")
            # form_phone = form.cleaned_data.get("phone")
            form_email = form.cleaned_data.get("email")
            form_subject = form.cleaned_data.get("subject")
            form_message = form.cleaned_data.get("message")

            subject = 'Feedback: %s' %(form_subject)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['contact@telegraph.ng']
            contact_message = " Name: %s \n Email: %s \n\n Message: \n\n %s" %(
            	form_fullname,
                # form_phone,
            	form_email,
            	form_message)

            send_mail(subject,
            	contact_message,
            	from_email,
            	to_email,
            	fail_silently=False)
            context = {
            	"opinion_list": Post.objects.active(),
            	"form": form,
            }
            return HttpResponseRedirect('/feedback-sent/')

    form_fullname = request.POST.get('fullname', '')
    # form_phone = request.POST.get('phone', '')
    form_email = request.POST.get('email', '')
    form_subject = request.POST.get('subject', '')
    form_message = request.POST.get('message', '')

    context = {
    	"opinion_list": Post.objects.active(),
    	"form": form,
    	"fullname": form_fullname,
        # "phone": form_phone,
    	"email": form_email,
    	"subject": form_subject,
    	"message": form_message,
    }
    return render(request, "feedback.html", context)


def feedback_sent(request):
	# queryset = Post.objects.active()
	form = FeedbackForm(request.POST or None)
	title = 'Message Sent Successfully'
	context = {
		"opinion_list": Post.objects.active(),
		"form": form,
	}
	return render(request, "feedback_sent.html", context)
