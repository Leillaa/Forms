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

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from survey.models import Survey

@login_required
def profile(request):
    user = request.user
    surveys = Survey.objects.filter(user=user).select_related('questionnaire').order_by('questionnaire__name')
    return render(request, 'users/profile.html', {
        'username': user.username,
        'date_joined': user.date_joined,
        'surveys': surveys
    })

