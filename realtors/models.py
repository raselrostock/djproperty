from datetime import datetime

from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save

from djproperty.utils import unique_slug_generator

class Realtor(models.Model):
    slug = models.SlugField('Slug', max_length=150, blank=True, unique=True)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_som = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'Realtor'
        verbose_name_plural = 'Realtors'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("realtors:realtor-detail", kwargs={"realtor_slug": self.slug})

def realtor_slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.name, instance.slug)


pre_save.connect(realtor_slug_save, sender=Realtor)
