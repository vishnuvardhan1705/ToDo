from django.http import HttpResponse
from django.shortcuts import render
from todo.models import tasks

def home(request):
    task = tasks.objects.filter(iscompleted=True).order_by('-updatedat')
    competed_task = tasks.objects.filter(iscompleted=False)
    context = {
        'task' : task,
        'competed_task':competed_task,
    }
    return render(request,'home.html',context)