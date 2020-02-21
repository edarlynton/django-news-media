try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from posts.models import Category, Post



def about(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/about.html", context)


def advertising(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/advertising.html", context)


def workforus(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/workforus.html", context)


def contact(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active().order_by("?")#.filter(category__title="Opinion")
	}
	return render(request, "others/contact.html", context)



def faq(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active().order_by("?")#.filter(category__title="Opinion")
	}
	return render(request, "others/faq.html", context)


def feedback(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active().order_by("?")#.filter(category__title="Opinion")
	}
	return render(request, "others/feedback.html", context)



def contributors_guide(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active().order_by("?")#.filter(category__title="Opinion")
	}
	return render(request, "others/contributors_guide.html", context)



def complaints(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/complaints.html", context)


def terms(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/terms.html", context)


def privacy(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/privacy.html", context)


def cookies(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/cookies.html", context)


def contributors(request):
	today = timezone.now().date()
	context = {
		"today": today,
		"opinion_list": Post.objects.active()#.filter(category__title="Opinion")
	}
	return render(request, "others/contributors_guide.html", context)



