from django.shortcuts import render
from .models import Standard, Subject, Lesson
from django.views.generic import ListView, DetailView, TemplateView, FormView
# Create your views here.


class StandardListView(ListView):

    context_object_name = 'standards'
    model = Standard
    template_name = 'standard_list_view.html'

class SubjectListView(DetailView):

    context_object_name = 'standards'
    model = Standard
    template_name = 'subject_list_view.html'


class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'lesson_list_view.html'


class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'lesson_details_view.html'