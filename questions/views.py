from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
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