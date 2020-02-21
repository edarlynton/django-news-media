from django.db import models

# Create your models here.


# class Feedback(models.Model):
#     fullname = models.CharField(max_length=120)
#     # phone = models.IntegerField(label='Phone')
#     email = models.EmailField()
#     subject = models.CharField(max_length=120, required=True)
#     message = models.TextField()

#     def __str__(self):
#     	return "%s - %s" %(self.email, self.subject)