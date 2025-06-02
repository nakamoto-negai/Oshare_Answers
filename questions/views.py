from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from questions.models import Question
from answers.forms import AnswerForm
from answers.models import Answer
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm

@login_required
def post_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_list')  # 質問一覧ページなどにリダイレクト
    else:
        form = QuestionForm()
    return render(request, 'questions/post_question.html', {'form': form})

def search_questions(request):
    query = request.GET.get('q')
    questions = Question.objects.all()
    if query:
        questions = questions.filter(title__icontains=query)
    return render(request, 'questions/search_questions.html', {'questions': questions, 'query': query})

def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions/question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'questions/question_detail.html', {
        'question': question,
        'form': form,
    })



