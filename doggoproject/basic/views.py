from django.shortcuts import render
from . import forms
from basic.models import Doggo

# Create your views here.

def index(request):
    doggo_list = Doggo.objects.order_by('dog_name')
    return_dict = {'doggo_list_object':doggo_list}
    return render(request,'basic/index.html', context=return_dict)

def form_name_view(request):
    form = forms.FormName()
    return render(request,'basic/forms.html',{'form':form})
