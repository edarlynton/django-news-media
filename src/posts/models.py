from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from markdown_deux import markdown
from comments.models import Comment




class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

    # def get_related(self, instance):
    #     product_one = self.get_queryset().filter(subcategory=instance.subcategory)
    #     product_two = self.get_queryset().filter(category=instance.category)
    #     qs = (product_one | product_two).exclude(id=instance.id).distinct()
    #     return qs


def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "posts/%s.%s" %(instance.id, extension)
    return "posts/%s/%s" %(instance.category, filename)
   

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    caption = models.CharField(max_length=120, null=True, blank=True)
    author = models.CharField(max_length=120, null=True, blank=True)
    briefing = models.CharField(max_length=360, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location,
            null=False,
            blank=False,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0, editable=False)
    width_field = models.IntegerField(default=0, editable=False)
    image_caption = models.CharField(max_length=360, null=True, blank=True)
    category = models.ForeignKey('Category', blank=False, null=False, on_delete=models.CASCADE)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish", "-updated", "-timestamp"]

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug, "cat_slug": self.category.slug})

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text) 

    def get_image_url(self):
        img = self.image.url
        return img

    def get_previous_object(self):
        previous_id = self.id - 1
        previous_obj = Post.objects.active().filter(id=previous_id)
        return previous_obj.first()

    def get_next_object(self):
        previous_id = self.id + 1
        previous_obj = Post.objects.active().filter(id=previous_id)
        return previous_obj.first()

    def get_random_object(self):
        # obj = Post.objects.active().filter(category=self.category).order_by('?')
        obj = Post.objects.active().order_by('?')
        return obj

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, new_slug=None)

pre_save.connect(pre_save_post, sender=Post)




class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title", "timestamp"]

    def get_absolute_url(self):
        return reverse('posts:category', kwargs={"slug": self.slug})


