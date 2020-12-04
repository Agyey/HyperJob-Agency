from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = r'signup\index.html'
