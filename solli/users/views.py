from django.shortcuts import render, redirect
from .forms import CustomUserForm

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
