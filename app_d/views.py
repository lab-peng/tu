import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import redirect, render

from django.contrib.auth import logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from app_d.forms import SampleModelForm, SearchForm
from .models import SampleModel


# custom error pages
def custom_error_403(request, exception):
    return render(request, 'errors/403.html', {})

def custom_error_404(request, exception): # Only works when debug set to False
    return render(request, 'errors/404.html', {})

def log_out(request):
    logout(request)
    return redirect('login') 

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required
def alpha(request):
    return render(request, 'app_d/alpha.html')


class SampleModelList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = SampleModel
    paginate_by = 5

    permission_required = ('app_d.view_samplemodel', )

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET:
            kwargs = {k: (self.request.GET.getlist(k) if k.endswith('__in') else self.request.GET.get(k))
            for k, v in self.request.GET.items() if v != '' and k != 'page' and k!='order_by'}
            queryset = queryset.filter(**kwargs).order_by(self.request.GET.get('order_by')) if self.request.GET.get('order_by') else queryset.filter(**kwargs)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SampleModelForm()
        context['search_form'] = SearchForm()
        return context

@login_required
@permission_required('app_d.add_samplemodel')
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