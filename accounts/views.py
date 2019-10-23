from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustromUserChangeForm, CustomUserCreationForm
from django.shortcuts import get_object_or_404
# from .models import User
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        # 1. 사용자가 보낸 내용 담아서
        form = CustromUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            # 2. 검증
            form.save()
            # 3. 반영
            return redirect('articles:index')
    else:
        form = CustromUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/form.html',context)

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/form.html',context)


def profile(request, account_pk):
    # user = User.objects.get(pk=account_pk)
    User = get_user_model()
    user = get_object_or_404(User,pk=account_pk)
    context = {
        'user_profile':user
    }
    return render(request,'accounts/profile.html',context)

def follow(request, account_pk):
    User = get_user_model()
    obama = get_object_or_404(User,pk=account_pk)
    if obama != request.user:
        if request.user in obama.followers.all():
            obama.followers.remove(request.user)
        else:
            obama.followers.add(request.user)
        return redirect('accounts:profile',account_pk)


