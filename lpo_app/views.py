from django.shortcuts import render,redirect
from .forms import Lpoform
from .models import lporecords

# Create your views here.
def lpo_list(request):
    context = {'lpo_list': lporecords.objects.all()}
    return render(request,"lpo_app/lpo_list.html",context)
 
def lpo_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Lpoform()
        else:
            lpo = lporecords.objects.get(pk=id)
            form = Lpoform(instance=lpo)
        return render(request,"lpo_app/lpo_form.html",{'form':form})
    else:
        if id == 0:
            form = Lpoform(request.POST)
        else:
            lpo = lporecords.objects.get(pk=id)
            form = Lpoform(request.POST,instance = lpo)
        if form.is_valid():
            form.save()
        return redirect('/list')
 
def lpo_delete(request,id):
    lpo = lporecords.objects.get(pk=id)
    lpo.delete()
    return redirect('/list')

def lpo_index(request):
    return render(request,"lpo_app/index.html")