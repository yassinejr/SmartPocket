from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profiles/')
    website_url = models.CharField(max_length=120, null=True, blank=True)
    facebook_url = models.CharField(max_length=120, null=True, blank=True)
    github_url = models.CharField(max_length=120, null=True, blank=True)
    instagram_url = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])
    print(kwargs)


post_save.connect(create_profile, sender=User)
