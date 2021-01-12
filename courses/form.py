from django.forms import ModelForm
from .models import Lesson

class Lessonform(ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_id', 'name', 'position', 'video', 'ppt', 'notes']
