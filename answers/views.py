
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from questions.models import Question

def search_questions(request):
    query = request.GET.get('q')
    questions = Question.objects.all()
    if query:
        questions = questions.filter(title__icontains=query)
    return render(request, 'answers/search_questions.html', {'questions': questions, 'query': query})
# Create your views here.



@login_required
def post_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('search_questions')
    else:
        form = AnswerForm()
    return render(request, 'answers/post_answer.html', {'form': form, 'question': question})
