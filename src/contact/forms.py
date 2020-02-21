from django import forms
# from .models import Contact
# from captcha.fields import ReCaptchaField

class FeedbackForm(forms.Form):
    fullname = forms.CharField(label='Name', max_length=120)
    # phone = forms.IntegerField(label='Phone')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=120, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    # captcha_answer = forms.CharField(max_length=30)

    # def clean_captcha_answer(self):
    # 	captcha = self.cleaned_data.get('captcha_answer')
    # 	if not captcha == '428DU':
    # 		raise forms.ValidationError("Your answer is incorrect.")
    # 	return captcha

    def clean_message(self):
        message = self.cleaned_data.get('message')
        num_words = len(message.split())
        if num_words < 4:
        	raise forms.ValidationError("Message is too short.")
        return message
