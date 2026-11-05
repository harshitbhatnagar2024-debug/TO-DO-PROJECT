from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import todo_table

def home(request):
    data = todo_table.objects.all()
    return render(request, 'home.html', {'data': data})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if not title or not description or len(title) > 100 or len(description) > 1000:
            return render(request, 'add_task.html')

        todo_table.objects.create(
            title=title,
            description=description,
        )
        return redirect('home')

    return render(request, 'add_task.html')


def edit_task(request, task_id):
    task = get_object_or_404(todo_table, id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if not title or not description or len(title) > 100 or len(description) > 1000:
            return render(request, 'edit_task.html', {'task': task})
        task.title = title
        task.description = description
        task.save()
        return redirect('home')

    return render(request, 'edit_task.html', {'task': task})


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(todo_table, id=task_id)
    task.delete()
    return redirect('home')

@require_POST
def task_completed(request, task_id):
    task = get_object_or_404(todo_table, id=task_id)
    task.done = request.POST.get("checkbox") == "on"
    task.save()
    return redirect('home')


