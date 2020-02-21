from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from pagedown.widgets import PagedownWidget

from .models import Post#, Newsletter


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "caption",
            "briefing",
            "image",
            "image_caption",
            "category",
            "content",
            "featured",
            "draft",
            "publish",
        ]




# class SignupForm(forms.ModelForm):
#     first_name = forms.CharField(label=_("First name"),
#                                max_length=30,
#                                widget=forms.TextInput(
#                                    attrs={'placeholder':
#                                               _('First name'),
#                                           'autofocus': 'autofocus'}))
#     last_name = forms.CharField(label=_("Last name"),
#                                max_length=30,
#                                widget=forms.TextInput(
#                                    attrs={'placeholder':
#                                               _('Last name'),
#                                           'autofocus': 'autofocus'}))

#     class Meta:
#         model = get_user_model()
#         fields = ['first_name', 'last_name']

#     def signup(self, request, user):
#         # user.first_name = self.cleaned_data['first_name']
#         # user.last_name = self.cleaned_data['last_name']
#         user.save()

