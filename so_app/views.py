from django.shortcuts import render,redirect
from .forms import Soform
from .models import sorecords

# Create your views here.
def so_list(request):
    context = {'so_list': sorecords.objects.all()}
    return render(request,"so_app/so_list.html",context)
 
def so_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Soform()
        else:
            so = sorecords.objects.get(pk=id)
            form = Soform(instance=so)
        return render(request,"so_app/so_form.html",{'form':form})
    else:
        if id == 0:
            form = Soform(request.POST)
        else:
            so = sorecords.objects.get(pk=id)
            form = Soform(request.POST,instance = so)
        if form.is_valid():
            form.save()
        return redirect('/so/list')
 
def so_delete(request,id):
    so = sorecords.objects.get(pk=id)
    so.delete()
    return redirect('/so/list')


