from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator

class RestaurantLocation(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=True) # optional
    category    = models.CharField(max_length=120, null=True, blank=True) # optional

    # auto_now_add represents the time the object was created
    timestamp   = models.DateTimeField(auto_now_add=True)

    # auto_now represents the time the object was last updated
    updated     = models.DateTimeField(auto_now=True)

    slug = models.SlugField(null=True, blank=True)

    # this method allows us to define an object name, so it's not
    # 'RestaurantLocation object'
    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
