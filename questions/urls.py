from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_question, name='post_question'),
    path('list/', views.question_list, name='question_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
]