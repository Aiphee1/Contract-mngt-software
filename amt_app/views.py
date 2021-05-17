from django.shortcuts import render,redirect
from .forms import Amtform
from .models import amtrecords

# Create your views here.
def amt_list(request):
    context = {'amt_list': amtrecords.objects.all()}
    return render(request,"amt_app/amt_list.html",context)
 
def amt_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Amtform()
        else:
            amt = amtrecords.objects.get(pk=id)
            form = Amtform(instance=amt)
        return render(request,"amt_app/amt_form.html",{'form':form})
    else:
        if id == 0:
            form = Amtform(request.POST)
        else:
            amt = amtrecords.objects.get(pk=id)
            form = Amtform(request.POST,instance = amt)
        if form.is_valid():
            form.save()
        return redirect('/amt/list')
 
def amt_delete(request,id):
    amt = amtrecords.objects.get(pk=id)
    amt.delete()
    return redirect('/amt/list')


