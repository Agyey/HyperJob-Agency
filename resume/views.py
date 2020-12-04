from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Resume
from django import forms


class ResumeForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)


class ResumeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, r'resume\index.html', context={'resumes': Resume.objects.all()})


class ResumeCreateView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            resume = Resume.objects.create(
                description=request.POST.get("description"),
                author_id=request.user.id
            )
            return redirect("/home")
        else:
            return HttpResponse(status=403)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, r'resume\resume.html', context={'form': ResumeForm})
        else:
            return HttpResponse(status=403)
