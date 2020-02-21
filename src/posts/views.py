try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm#, NewsletterForm
from .models import Category, Post



def home(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = queryset_list.filter(featured=True).first()
	object_list = queryset_list.filter(featured=True)
	news_list = queryset_list.filter(category__title="News")
	more_list = queryset_list.filter(category__title="More")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	opinion_list = queryset_list.filter(category__title="Opinion")
	sport_list = queryset_list.filter(Q(category__title="Sport") | Q(category__title="Football") | Q(category__title="Football-Transfer")).distinct()
	business_list = queryset_list.filter(category__title="Business")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(category__title="Entertainment")
	politics_list = queryset_list.filter(category__title="Politics")
	nigeria_list = queryset_list.filter(category__title="Nigeria")
	# africa_list = queryset_list.filter(category__title="Africa")
	world_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Africa")).distinct()
	technology_list = queryset_list.filter(category__title="Technology")
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	metro_list = queryset_list.filter(category__title="Metro")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	education_list = queryset_list.filter(category__title="Education")
	health_list = queryset_list.filter(category__title="Health")
	property_list = queryset_list.filter(category__title="Property")	
	defender_list = queryset_list.filter(category__title="Defender")

	context = {
		"today": today,
		"query": query,
		"object_list": object_list,
		"news_list": news_list,
		"more_list": more_list,
		"spotlight_list": spotlight_list,
		"opinion_list": opinion_list,
		"sport_list": sport_list,
		"business_list": business_list,
		"lifestyle_list": lifestyle_list, 
		"politics_list": politics_list,
		"nigeria_list": nigeria_list,
		# "africa_list": africa_list,
		"world_list": world_list,
		"technology_list": technology_list,
		"sponsored_list": sponsored_list,
		"metro_list": metro_list,
		"entertainment_list": entertainment_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
		"education_list": education_list,
		"health_list": health_list,
		"defender_list": defender_list,
		"property_list": property_list,
	}
	return render(request, "home.html", context)


def world(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = queryset_list.filter(featured=True).first()
	object_list = queryset_list.filter(featured=True)
	news_list = queryset_list.filter(category__title="News")
	more_list = queryset_list.filter(category__title="More")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	opinion_list = queryset_list.filter(category__title="Opinion")
	sport_list = queryset_list.filter(Q(category__title="Sport") | Q(category__title="Football") | Q(category__title="Football-Transfer")).distinct()
	business_list = queryset_list.filter(category__title="Business")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(category__title="Entertainment")
	politics_list = queryset_list.filter(category__title="Politics")
	nigeria_list = queryset_list.filter(category__title="Nigeria")
	# africa_list = queryset_list.filter(category__title="Africa")
	world_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Africa")).distinct()
	technology_list = queryset_list.filter(category__title="Technology")
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	metro_list = queryset_list.filter(category__title="Metro")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	education_list = queryset_list.filter(category__title="Education")
	health_list = queryset_list.filter(category__title="Health")
	property_list = queryset_list.filter(category__title="Property")	
	defender_list = queryset_list.filter(category__title="Defender")

	context = {
		"today": today,
		"query": query,
		"object_list": object_list,
		"news_list": news_list,
		"more_list": more_list,
		"spotlight_list": spotlight_list,
		"opinion_list": opinion_list,
		"sport_list": sport_list,
		"business_list": business_list,
		"lifestyle_list": lifestyle_list, 
		"politics_list": politics_list,
		"nigeria_list": nigeria_list,
		# "africa_list": africa_list,
		"world_list": world_list,
		"technology_list": technology_list,
		"sponsored_list": sponsored_list,
		"metro_list": metro_list,
		"entertainment_list": entertainment_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
		"education_list": education_list,
		"health_list": health_list,
		"defender_list": defender_list,
		"property_list": property_list,
	}
	return render(request, "world_page.html", context)


def nigeria(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = queryset_list.filter(featured=True).first()
	object_list = queryset_list.filter(featured=True)
	news_list = queryset_list.filter(category__title="News")
	more_list = queryset_list.filter(category__title="More")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	opinion_list = queryset_list.filter(category__title="Opinion")
	sport_list = queryset_list.filter(Q(category__title="Sport") | Q(category__title="Football") | Q(category__title="Football-Transfer")).distinct()
	business_list = queryset_list.filter(category__title="Business")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(category__title="Entertainment")
	politics_list = queryset_list.filter(category__title="Politics")
	nigeria_list = queryset_list.filter(category__title="Nigeria")
	# africa_list = queryset_list.filter(category__title="Africa")
	world_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Africa")).distinct()
	technology_list = queryset_list.filter(category__title="Technology")
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	metro_list = queryset_list.filter(category__title="Metro")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	education_list = queryset_list.filter(category__title="Education")
	health_list = queryset_list.filter(category__title="Health")
	property_list = queryset_list.filter(category__title="Property")	
	defender_list = queryset_list.filter(category__title="Defender")

	context = {
		"today": today,
		"query": query,
		"object_list": object_list,
		"news_list": news_list,
		"more_list": more_list,
		"spotlight_list": spotlight_list,
		"opinion_list": opinion_list,
		"sport_list": sport_list,
		"business_list": business_list,
		"lifestyle_list": lifestyle_list, 
		"politics_list": politics_list,
		"nigeria_list": nigeria_list,
		# "africa_list": africa_list,
		"world_list": world_list,
		"technology_list": technology_list,
		"sponsored_list": sponsored_list,
		"metro_list": metro_list,
		"entertainment_list": entertainment_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
		"education_list": education_list,
		"health_list": health_list,
		"defender_list": defender_list,
		"property_list": property_list,
	}
	return render(request, "nigeria_page.html", context)


def politics(request, cat_slug=None):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = queryset_list.filter(featured=True).first()
	object_list = queryset_list.filter(featured=True)
	news_list = queryset_list.filter(category__title="News")
	more_list = queryset_list.filter(category__title="More")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	opinion_list = queryset_list.filter(category__title="Opinion")
	sport_list = queryset_list.filter(Q(category__title="Sport") | Q(category__title="Football") | Q(category__title="Football-Transfer")).distinct()
	business_list = queryset_list.filter(category__title="Business")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(category__title="Entertainment")
	politics_list = queryset_list.filter(category__title="Politics")
	nigeria_list = queryset_list.filter(category__title="Nigeria")
	# africa_list = queryset_list.filter(category__title="Africa")
	world_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Africa")).distinct()
	technology_list = queryset_list.filter(category__title="Technology")
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	metro_list = queryset_list.filter(category__title="Metro")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	education_list = queryset_list.filter(category__title="Education")
	health_list = queryset_list.filter(category__title="Health")
	property_list = queryset_list.filter(category__title="Property")	
	defender_list = queryset_list.filter(category__title="Defender")

	context = {
		"today": today,
		"query": query,
		"object_list": object_list,
		"news_list": news_list,
		"more_list": more_list,
		"spotlight_list": spotlight_list,
		"opinion_list": opinion_list,
		"sport_list": sport_list,
		"business_list": business_list,
		"lifestyle_list": lifestyle_list, 
		"politics_list": politics_list,
		"nigeria_list": nigeria_list,
		# "africa_list": africa_list,
		"world_list": world_list,
		"technology_list": technology_list,
		"sponsored_list": sponsored_list,
		"metro_list": metro_list,
		"entertainment_list": entertainment_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
		"education_list": education_list,
		"health_list": health_list,
		"defender_list": defender_list,
		"property_list": property_list,
	}
	return render(request, "politics_page.html", context)



def opinion(request, cat_slug=None):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = queryset_list.filter(featured=True).first()
	object_list = queryset_list.filter(featured=True)
	news_list = queryset_list.filter(category__title="News")
	more_list = queryset_list.filter(category__title="More")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	opinion_list = queryset_list.filter(category__title="Opinion")
	sport_list = queryset_list.filter(Q(category__title="Sport") | Q(category__title="Football") | Q(category__title="Football-Transfer")).distinct()
	business_list = queryset_list.filter(category__title="Business")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(category__title="Entertainment")
	politics_list = queryset_list.filter(category__title="Politics")
	nigeria_list = queryset_list.filter(category__title="Nigeria")
	# africa_list = queryset_list.filter(category__title="Africa")
	world_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Africa")).distinct()
	technology_list = queryset_list.filter(category__title="Technology")
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	metro_list = queryset_list.filter(category__title="Metro")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	education_list = queryset_list.filter(category__title="Education")
	health_list = queryset_list.filter(category__title="Health")
	property_list = queryset_list.filter(category__title="Property")	
	defender_list = queryset_list.filter(category__title="Defender")

	context = {
		"today": today,
		"query": query,
		"object_list": object_list,
		"news_list": news_list,
		"more_list": more_list,
		"spotlight_list": spotlight_list,
		"opinion_list": opinion_list,
		"sport_list": sport_list,
		"business_list": business_list,
		"lifestyle_list": lifestyle_list, 
		"politics_list": politics_list,
		"nigeria_list": nigeria_list,
		# "africa_list": africa_list,
		"world_list": world_list,
		"technology_list": technology_list,
		"sponsored_list": sponsored_list,
		"metro_list": metro_list,
		"entertainment_list": entertainment_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
		"education_list": education_list,
		"health_list": health_list,
		"defender_list": defender_list,
		"property_list": property_list,
	}
	return render(request, "opinion_page.html", context)



def business(request, cat_slug=None):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = queryset_list.filter(featured=True).first()
	object_list = queryset_list.filter(featured=True)
	news_list = queryset_list.filter(category__title="News")
	more_list = queryset_list.filter(category__title="More")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	opinion_list = queryset_list.filter(category__title="Opinion")
	sport_list = queryset_list.filter(Q(category__title="Sport") | Q(category__title="Football") | Q(category__title="Football-Transfer")).distinct()
	business_list = queryset_list.filter(category__title="Business")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(category__title="Entertainment")
	politics_list = queryset_list.filter(category__title="Politics")
	nigeria_list = queryset_list.filter(category__title="Nigeria")
	# africa_list = queryset_list.filter(category__title="Africa")
	world_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Africa")).distinct()
	technology_list = queryset_list.filter(category__title="Technology")
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	metro_list = queryset_list.filter(category__title="Metro")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	education_list = queryset_list.filter(category__title="Education")
	health_list = queryset_list.filter(category__title="Health")
	property_list = queryset_list.filter(category__title="Property")	
	defender_list = queryset_list.filter(category__title="Defender")

	context = {
		"today": today,
		"query": query,
		"object_list": object_list,
		"news_list": news_list,
		"more_list": more_list,
		"spotlight_list": spotlight_list,
		"opinion_list": opinion_list,
		"sport_list": sport_list,
		"business_list": business_list,
		"lifestyle_list": lifestyle_list, 
		"politics_list": politics_list,
		"nigeria_list": nigeria_list,
		# "africa_list": africa_list,
		"world_list": world_list,
		"technology_list": technology_list,
		"sponsored_list": sponsored_list,
		"metro_list": metro_list,
		"entertainment_list": entertainment_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
		"education_list": education_list,
		"health_list": health_list,
		"defender_list": defender_list,
		"property_list": property_list,
	}
	return render(request, "business_page.html", context)



def entertainment(request, cat_slug=None):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = queryset_list.filter(featured=True).first()
	object_list = queryset_list.filter(featured=True)
	news_list = queryset_list.filter(category__title="News")
	more_list = queryset_list.filter(category__title="More")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	opinion_list = queryset_list.filter(category__title="Opinion")
	sport_list = queryset_list.filter(Q(category__title="Sport") | Q(category__title="Football") | Q(category__title="Football-Transfer")).distinct()
	business_list = queryset_list.filter(category__title="Business")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(category__title="Entertainment")
	politics_list = queryset_list.filter(category__title="Politics")
	nigeria_list = queryset_list.filter(category__title="Nigeria")
	# africa_list = queryset_list.filter(category__title="Africa")
	world_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Africa")).distinct()
	technology_list = queryset_list.filter(category__title="Technology")
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	metro_list = queryset_list.filter(category__title="Metro")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	education_list = queryset_list.filter(category__title="Education")
	health_list = queryset_list.filter(category__title="Health")
	property_list = queryset_list.filter(category__title="Property")	
	defender_list = queryset_list.filter(category__title="Defender")

	context = {
		"today": today,
		"query": query,
		"object_list": object_list,
		"news_list": news_list,
		"more_list": more_list,
		"spotlight_list": spotlight_list,
		"opinion_list": opinion_list,
		"sport_list": sport_list,
		"business_list": business_list,
		"lifestyle_list": lifestyle_list, 
		"politics_list": politics_list,
		"nigeria_list": nigeria_list,
		# "africa_list": africa_list,
		"world_list": world_list,
		"technology_list": technology_list,
		"sponsored_list": sponsored_list,
		"metro_list": metro_list,
		"entertainment_list": entertainment_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
		"education_list": education_list,
		"health_list": health_list,
		"defender_list": defender_list,
		"property_list": property_list,
	}
	return render(request, "entertainment_page.html", context)



def sport(request, cat_slug=None):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	sport_list = queryset_list.filter(category__title="Sport")
	sport_football_list = queryset_list.filter(category__title="Football")
	sport_transfer_list = queryset_list.filter(category__title="Football-Transfer")
	news_list = queryset_list.filter(Q(category__title="World") | Q(category__title="Nigeria") | Q(category__title="Politics") | Q(category__title="Business")).distinct()
	more_list = queryset_list.filter(category__title="More")	
	opinion_list = queryset_list.filter(category__title="Opinion")	
	politics_list = queryset_list.filter(category__title="Politics")
	spotlight_list = queryset_list.filter(category__title="Spotlight")
	lifestyle_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Entertainment") | Q(category__title="Travel")).distinct()
	entertainment_list = queryset_list.filter(Q(category__title="Lifestyle") | Q(category__title="Entertainment") | Q(category__title="Travel")).distinct()
	sponsored_list = queryset_list.filter(category__title="Sponsored")
	defender_list = queryset_list.filter(category__title="Defender")
	video_list = queryset_list.filter(category__title="Video")
	picture_list = queryset_list.filter(category__title="Picture")
	cartoon_list = queryset_list.filter(category__title="Cartoon")
	query = queryset_list.filter(featured=True).first()

	context = {
		"today": today,
		"query": query,
		# "object_list": queryset_list,
		"news_list": news_list,
		"more_list": more_list,
		"sport_list": sport_list,
		"sport_football_list": sport_football_list,
		"sport_transfer_list": sport_transfer_list,
		"opinion_list": opinion_list,
		"politics_list": politics_list,
		"spotlight_list": spotlight_list,
		"lifestyle_list": lifestyle_list, 
		"entertainment_list": entertainment_list,
		"sponsored_list": sponsored_list,
		"defender_list": defender_list,
		"video_list": video_list,
		"picture_list": picture_list,
		"cartoon_list": cartoon_list,
	}
	return render(request, "sport_page.html", context)









def detail(request, slug=None, cat_slug=None):
	today = timezone.now().date()
	queryset_list = Post.objects.active()

	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)

	if not request.user.is_authenticated:
		if request.POST:
			messages.success(request, "<i>Please kindly <a href='/accounts/login/'>login</a> or <a href='/accounts/signup/'>signup</a> to post comment.</i>", extra_tags='html_safe')
	else:
		if form.is_valid():
			c_type = form.cleaned_data.get("content_type")
			content_type = ContentType.objects.get(model=c_type)
			obj_id = form.cleaned_data.get('object_id')
			content_data = form.cleaned_data.get("content")
			parent_obj = None
			try:
				parent_id = int(request.POST.get("parent_id"))
			except:
				parent_id = None

			if parent_id:
				parent_qs = Comment.objects.filter(id=parent_id)
				if parent_qs.exists() and parent_qs.count() == 1:
					parent_obj = parent_qs.first()


			new_comment, created = Comment.objects.get_or_create(
								user = request.user,
								content_type= content_type,
								object_id = obj_id,
								content = content_data,
								parent = parent_obj,
							)
			return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	comments = instance.comments
	context = {
		"today": today,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form":form,
		"related_list": queryset_list.filter(category=instance.category).exclude(id=instance.id),
		"queryset_list": queryset_list,
		"sponsored_list": queryset_list.filter(category__title="Sponsored")
	}
	return render(request, "detail.html", context)






def post_create(request):
	today = timezone.now().date()
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
		"today": today,
	}
	return render(request, "post_form.html", context)



def post_update(request, slug=None, cat_slug=None):
	today = timezone.now().date()
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
		"today": today,
	}
	return render(request, "post_form.html", context)



def post_delete(request, slug=None, cat_slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:home")






