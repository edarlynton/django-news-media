from django.contrib import admin
# from django.db.models.signals import pre_save
# from django.utils.text import slugify

from .models import Post, Category


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "caption", "featured", "category", "draft", "publish", "timestamp"]
	# list_display_links = ["updated"]
	list_editable = ["featured", "draft"]
	list_filter = ["featured", "draft", "timestamp", "publish", "category"]
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ["title", "content", "user"]
	class Meta:
		model = Post



	# def create_slug(instance, new_slug=None):
	#     slug = slugify(instance.title)
	#     if new_slug is not None:
	#         slug = new_slug
	#     qs = Post.objects.filter(slug=slug).order_by("-id")
	#     exists = qs.exists()
	#     if exists:
	#         new_slug = "%s-%s" %(slug, qs.first().id)
	#         return create_slug(instance, new_slug=new_slug)
	#     return slug


	# def pre_save_post(sender, instance, *args, **kwargs):
	#     if not instance.slug:
	#         instance.slug = create_slug(instance, new_slug=None)

	# pre_save.connect(pre_save_post, sender=Post)


admin.site.register(Post, PostModelAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'active']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['active',]
    list_editable = ['active']
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)