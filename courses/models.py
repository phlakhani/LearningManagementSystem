from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=400,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save( *args, **kwargs)


class Subject(models.Model):
    subject_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='subject')
    image = models.ImageField(upload_to='Subject_images', verbose_name='subject_image')
    description = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save( *args, **kwargs)


class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100, unique=True)
    standard =  models.ForeignKey(Standard, on_delete=models.CASCADE,)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lesson')
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    position = models.PositiveSmallIntegerField(verbose_name='Chapter No.')
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to='lessons/video', verbose_name='Video', blank=True, null=True)
    ppt =   models.FileField(upload_to='lessons/ppt', verbose_name='Presentations', blank=True)
    notes = models.FileField(upload_to='lessons/notes', verbose_name='Notes', blank=True)

    class Meta:
        ordering = ['position']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save( *args, **kwargs)