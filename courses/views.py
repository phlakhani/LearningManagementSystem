from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Standard, Subject, Lesson
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from .form import Lessonform
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

class LessonCreateView(CreateView):

    form_class = Lessonform
    context_object_name = 'subjects'
    model = Subject
    template_name = 'lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy ('courses:lesson_list', kwargs={'standard':standard.slug, 'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.objects = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
