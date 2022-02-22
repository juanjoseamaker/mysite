from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from .forms import TaskForm

def delete(response):
    return render(response, 'delete_form.html')

def delete_id(request, id):
    if request.method == 'POST':
        try:
            item = Task.objects.get(id=int(id))
            item.delete()
        except ValueError:
            return HttpResponse('Failed to delete task', status=500)
        except Task.DoesNotExist:
            return HttpResponse('Failed to delete task, task does not exist', status=500)
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            item = Task(
                title=form.cleaned_data['title'],
                date=form.cleaned_data['date'],
                description=form.cleaned_data['description'],
                complete=form.cleaned_data['complete']
            )
            item.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()

    return render(request, 'add_form.html', {'form': form})

def index(response):
    tasks = Task.objects.all().order_by('date')
    return render(response, 'index.html', {'tasks': tasks.iterator()})
