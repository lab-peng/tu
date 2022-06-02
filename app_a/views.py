import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Project, Document
from .forms import ProjectUpdateForm

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
        # print(self.request.POST, self.request.FILES)
        data = []
        for f in self.request.FILES.getlist('file'):
            d = Document.objects.create(file=f, project=self.get_object())
            data.append(d)
        data = [{'d_pk': d.pk, 'd_file': d.file.url, 'd_filename':d.filename } for d in data]
        return JsonResponse(data, safe=False)


class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'app_a/project_update.html'
    success_url = '/project_list/'

def upload_file(request, pk):
    pass # todo finish this view
    # data = []
    # for f in request.FILES.getlist('file'):
    #     d = Document.objects.create(file=f, project=self.get_object())
    #     data.append(d)
    # data = [{'d_pk': d.pk, 'd_file': d.file.url, 'd_filename':d.filename } for d in data]
    # return JsonResponse(data, safe=False)

def delete_file(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.file.delete()
    doc.delete()
    return JsonResponse({'status': 1}, safe=False)






def tianditu(request):
    return render(request, 'app_a/tdt.html')



