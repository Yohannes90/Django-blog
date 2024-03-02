from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account has been successfully created, Welcome { username }!")
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
