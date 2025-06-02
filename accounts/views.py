from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from coupons.models import Coupon
from questions.models import Question
from answers.models import Answer
from purchases.models import Purchase  # または orders.models.Order など、購入履歴のモデル名に合わせてください

User = get_user_model()

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    coupons = Coupon.objects.filter(user=user)
    questions = Question.objects.filter(user=user).order_by('-created_at')
    answers = Answer.objects.filter(user=user).order_by('-created_at')
    purchases = Purchase.objects.filter(user=user).order_by('-purchased_at')
    return render(request, 'accounts/profile.html', {
        'user': user,
        'coupons': coupons,
        'questions': questions,
        'answers': answers,
        'purchases': purchases,
    })
# Create your views here.
