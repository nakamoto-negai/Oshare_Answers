from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_questions, name='search_questions'),
    path('answer/<int:question_id>/', views.post_answer, name='post_answer'),
]