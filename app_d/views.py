import json
# from re import M
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import redirect, render
from app_d.forms import SampleModelForm, SearchForm
from .models import SampleModel

from django.http import QueryDict
import urllib

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class SampleModelList(ListView):
    model = SampleModel

    # def get(request, *args, **kwargs):
    #     print('hello')
    #     return super().get(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET:
            kwargs = {k: v for k, v in self.request.GET.items()}
            print(kwargs)
            queryset = queryset.filter(**kwargs)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SampleModelForm()
        context['search_form'] = SearchForm()
        return context
    
def create_update(request):
    # request should be ajax and method should be POST.
    if is_ajax(request) and request.method == "POST":
        post_ids = request.POST.get('post_ids')
        if post_ids:
            post_ids = post_ids.split(',') if ',' in post_ids else [post_ids,]
        # create
        if not post_ids:
            form = SampleModelForm(request.POST)
            if form.is_valid():
                instance = form.save()
                instance = model_to_dict(instance)
                return JsonResponse({"instance": instance}, status=200)
            else:
                errors = {k: v for k , v in form.errors.items()}
                return JsonResponse({"errors": errors})  
        # update
        elif len(post_ids) == 1:
            form = SampleModelForm(request.POST, instance=SampleModel.objects.get(pk=int(post_ids[0])))
            if form.is_valid():
                instance = form.save()
                instance = model_to_dict(instance)
                return JsonResponse({"instance": instance}, status=200)
            else:
                errors = {k: v for k , v in form.errors.items()}
                return JsonResponse({"errors": errors})
    return JsonResponse({"errors": ""}, status=400)


def get_update_info(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        ids = [int(id) for id in json.loads(ids)]
        instances = SampleModel.objects.filter(id__in=ids)
        instances = [model_to_dict(instance) for instance in instances]
        return JsonResponse({'status':1, 'instances': instances})
    else:
        return JsonResponse({'status':0})   

def delete(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        ids = [int(id) for id in json.loads(ids)]
        instances = SampleModel.objects.filter(id__in=ids)
        instances.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})   