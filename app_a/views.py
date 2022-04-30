import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Project, Document

def index(request):
    return render(request, 'app_a/index.html')

class ProjectList(ListView):
    model = Project

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hello'] = 'Hello World!'
    #     return context

class ProjectDetail(DetailView):
    model = Project
    template_name = 'app_a/project_detail.html'


    def post(self, request, *args, **kwargs):
        for f in self.request.FILES.getlist('file'):
            Document.objects.create(file=f, project=self.get_object())
        documents = [{'d_pk': d.pk, 'd_file': d.file.url } for d in self.get_object().document_set.all()]
        print(documents)
        # return JsonResponse(documents, safe=False)
        return redirect('app_a:project_detail', pk=self.get_object().pk)


def delete_file(request, pk, doc_pk):
    doc = Document.objects.get(pk=doc_pk)
    doc.file.delete()
    doc.delete()
    return redirect('app_a:project_detail', pk=pk)

def del_file(request):
    data = json.loads(request.body.decode('utf-8'))
    pro_pk = data.get('pro_pk')
    doc_pk = data.get('doc_pk')
    print(pro_pk, doc_pk)
    doc = Document.objects.get(pk=doc_pk)
    doc.file.delete()
    doc.delete()
    return JsonResponse({'status': 'success'})

# figure out how to remove the element from the list item clicked delete
# TODO find a youtube video on how to crud a todo list


def test(request):
    return render(request, 'app_a/test.html')



