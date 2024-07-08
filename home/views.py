from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import task
from .forms import taskform
# Create your views here.
def index(request):
    obj = task.objects.all()
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = taskform()
    return render(request, 'home.html', {'obj': obj, 'form': form})


def edit(request,pk):
    instance_to_be_edited=task.objects.get(pk=pk)
    if request.POST:
        frm = taskform(request.POST,instance=instance_to_be_edited)
        if frm.is_valid:
            frm.save()
            return redirect('/')
    else:
         frm = taskform(instance=instance_to_be_edited)
    return render(request,"edit.html",{'frm':frm})
def delete(request, pk):
    deleted = get_object_or_404(task, pk=pk)
    if request.POST:
        deleted.delete()
        return redirect('/')
    return render(request, "delete.html",{'deleted':deleted})