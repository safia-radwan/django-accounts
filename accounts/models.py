from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created :
            profile.objects.create(user=instance)


        