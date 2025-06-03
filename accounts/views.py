from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from coupons.models import Coupon
from questions.models import Question
from answers.models import Answer
from orders.models import Order # または orders.models.Order など、購入履歴のモデル名に合わせてください
from items.models import Recommendation
User = get_user_model()

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # ホーム画面などにリダイレクト
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})

def signout_view(request):
    logout(request)
    return redirect('signin')


@login_required
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    coupons = Coupon.objects.filter(users=user)
    questions = Question.objects.filter(user=user).order_by('-created_at')
    answers = Answer.objects.filter(user=user).order_by('-created_at')
    orders = Order.objects.filter(user=user).order_by('-ordered_at')
    recommendations = Recommendation.objects.filter(recommended_to=user).select_related('item')
    return render(request, 'accounts/profile.html', {
        'user': user,
        'coupons': coupons,
        'questions': questions,
        'answers': answers,
        'orders': orders,
        'recommendations': recommendations,
    })
# Create your views here.
