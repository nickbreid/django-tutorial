from django.db import models

class RestaurantLocation(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=True) # optional
    category    = models.CharField(max_length=120, null=True, blank=True) # optional

    # auto_now_add represents the time the object was created
    timestamp   = models.DateTimeField(auto_now_add=True)

    # auto_now represents the time the object was last updated
    updated     = models.DateTimeField(auto_now=True)

    # this method allows us to define an object name, so it's not
    # 'RestaurantLocation object'
    def __str__(self):
        return self.name
