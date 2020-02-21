from django.shortcuts import render
from .forms import SignUpForm
from .models import SignUp
from posts.models import Post
# from datetime import datetime
from django.utils import timezone


def newsletter(request):
    form = SignUpForm(request.POST or None)
    
    today = timezone.now().date() # datetime.now()

    context = {
        'title': "Subscribe now for breaking news",
        'form': form,
        "opinion_list": Post.objects.active()[0:6],
    }
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        query = SignUp.objects.filter(email=form_email)
        if query:
            title = "Already Subscribed"
        else:
            form.save()
            title = "Subscription Confirmed"
        
        context = {
            'title': title,
            "opinion_list": Post.objects.active()[0:6],
        }
    return render(request, 'others/newsletter.html', context)


