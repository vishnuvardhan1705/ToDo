from django.shortcuts import render,redirect,get_object_or_404
from .models import tasks

def addtask(request):
    task = request.POST['task']
    tasks.objects.create(task=task)
    return redirect('home')

def markasdone(request,pk):
    task = get_object_or_404(tasks,pk=pk)
    task.iscompleted=True
    task.save()
    return redirect('home')

def markasundone(request,pk):
    task = get_object_or_404(tasks,pk=pk)
    task.iscompleted=False
    task.save()
    return redirect('home')

def edittask(request,pk):
    gettask = get_object_or_404(tasks,pk=pk)
    if request.method == 'POST':
        newtask = request.POST['task']
        gettask.task = newtask
        gettask.save()
        return redirect('home')
    else:
        context = {
            'gettask':gettask,
        }
        return render(request,"edittask.html",context)
    
def delettask(request,pk):
    task = get_object_or_404(tasks,pk=pk)
    task.delete()
    return redirect('home')