from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import LoginForm

@require_POST
def login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        print('ok')
        return redirect('/')
    return redirect('/')