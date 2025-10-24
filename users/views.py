from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


def logout(request):
    return render(request, 'users/logged_out.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('units:index')
    template_name = 'users/signup.html'

