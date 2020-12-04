from django import forms
from django.views import View
from django.shortcuts import render


class HomeForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, r'home\index.html', context={'form': HomeForm, 'user': request.user})
