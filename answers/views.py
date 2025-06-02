
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from questions.models import Question





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
