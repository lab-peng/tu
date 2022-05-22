from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from .forms import ProfileForm
from .models import Profile

def index(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app_e/update/9/')
        else:
            print(form.errors)
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'app_e/index.html', context)


def update(request, pk):
    instance = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(instance=instance)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(f'/app_e/update/{pk}/')
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'app_e/update.html', context)


# class ProfileCreate(CreateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'app_e/index.html'
#     success_url = '/app_e/'

