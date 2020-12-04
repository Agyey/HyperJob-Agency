from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Vacancy
from django import forms


class VacancyForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)


class VacancyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, r'vacancy\index.html', context={'vacancies': Vacancy.objects.all()})

class VacancyCreateView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            Vacancy.objects.create(
                description=request.POST.get("description"),
                author_id=request.user.id
            )
            return redirect("/home")
        else:
            return HttpResponse(status=403)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return render(request, r'vacancy\vacancy.html', context={'form': VacancyForm})
        else:
            return HttpResponse(status=403)
