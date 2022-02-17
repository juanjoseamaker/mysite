from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from .forms import TaskForm

def delete(response):
    return render(response, 'delete.html')

def delete_id(request, id):
    if request.method == 'POST':
        try:
            item = Task.objects.get(id=int(id))
            item.delete()
        except ValueError:
            return HttpResponse('Failed to delete task')
        except Task.DoesNotExist:
            return HttpResponse('Failed to delete task, that task does not exist')
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

    return render(request, 'task.html', {'form': form})

def index(reponse):
    page = '''
        <html>
        <head><title>MySite</title></head>
        <body>
        <h1>Tasks</h1><a href="/add">Add</a> <a href="/delete">Delete</a><br>
    '''

    tasks = Task.objects.all()
    for item in tasks.iterator():
        page += '''
        <h4>Task #{}</h4>
        <h4>Title: {}</h4>
        <h4>Description: {}</h4>
        <h4>Date: {}</h4>
        <h4>Complete: {}</h4>
        <br>
        '''.format(item.id, item.title, item.description, item.date.isoformat(), item.complete)
    
    page += '''
        </body>
        </html>
    '''

    return HttpResponse(page)
