import json

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.core import serializers
from .forms import FriendForm
from .models import Friend

from django.views import View


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def indexView(request):
    form = FriendForm()
    friends = Friend.objects.all()
    return render(request, "index.html", {"form": form, "friends": friends})


def create_update_friend(request):
    # request should be ajax and method should be POST.
    if is_ajax(request) and request.method == "POST":
        # create
        if not request.POST.get('sid') or not Friend.objects.filter(pk=request.POST.get('sid')).exists():
            print(0)
            form = FriendForm(request.POST)
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                instance = {k: v for k , v in instance.__dict__.items() if not k.startswith('_')}
                print(instance)
                return JsonResponse({"instance": instance}, status=200)
            else:
                errors = {k: v for k , v in form.errors.items()}
                return JsonResponse({"errors": errors})  
        # update
        else:
            print(1)
            form = FriendForm(request.POST, instance=Friend.objects.get(pk=request.POST.get('sid')))
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                instance = {k: v for k , v in instance.__dict__.items() if not k.startswith('_')}
                print(instance)
                return JsonResponse({"instance": instance}, status=200)
            else:
                errors = {k: v for k , v in form.errors.items()}
                return JsonResponse({"errors": errors})
    return JsonResponse({"errors": ""}, status=400)


def delete_friend(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s = Friend.objects.get(pk=int(id))
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    

def edit_friend(request):  # Only for populating the eidt form
    if request.method == 'POST':
        id = request.POST.get('sid')
        instance = Friend.objects.get(pk=int(id))
        instance = {k: v for k , v in instance.__dict__.items() if not k.startswith('_')}
        return JsonResponse({'status':1, 'instance':instance})
    else:
        return JsonResponse({'status':0})    


















# BONUS CBV
def checkNickName(request):
    # request should be ajax and method should be GET.
    if is_ajax(request) and request.method == "GET":
        # get the nick name from the client side.
        nick_name = request.GET.get("nick_name", None)
        # check for the nick name in the database.
        if Friend.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    



class FriendView(View):
    form_class = FriendForm
    template_name = "index.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        friends = Friend.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "friends": friends})

    def post(self, *args, **kwargs):
        # request should be ajax and method should be POST.
        if is_ajax(self.request) and self.request.method == "POST":
            # get the form data
            form = self.form_class(self.request.POST)
            # save the data and after fetch the object in instance
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)

        # some error occured
        return JsonResponse({"error": ""}, status=400)
