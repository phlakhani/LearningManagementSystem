from django.urls import path
from .views import StandardListView, SubjectListView, LessonListView, LessonDetailView

app_name = 'courses'

urlpatterns = [
    path('', StandardListView.as_view(), name='standard-list'),
    path('<slug:slug>/', SubjectListView.as_view(), name='subject_list'),
    path('<str:standard>/<slug:slug>/', LessonListView.as_view(), name='lesson_list'),
    path('<str:standard>/<str:subject>/<slug:slug>/', LessonDetailView.as_view(), name='lesson_detail'),
]