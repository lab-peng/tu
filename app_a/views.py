from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Project, Document

def index(request):
    return render(request, 'app_a/index.html')

class ProjectDetail(DetailView):
    model = Project
    template_name = 'app_a/project_detail.html'


    def post(self, request, *args, **kwargs):
        for f in self.request.FILES.getlist('file'):
            Document.objects.create(file=f, project=self.get_object())
        return redirect('app_a:project_detail', pk=self.get_object().pk)


def delete_file(request, pk, doc_pk):
    doc = Document.objects.get(pk=doc_pk)
    doc.file.delete()
    doc.delete()
    return redirect('app_a:project_detail', pk=pk)



