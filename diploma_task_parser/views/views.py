from django.shortcuts import render


def home(request):
    return render(request, 'diploma_task_parser/home.html')
