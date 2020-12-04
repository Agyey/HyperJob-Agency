from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = r'login\index.html'
