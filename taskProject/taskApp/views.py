from django.shortcuts import render
from taskApp.models import Tasks
from taskApp.tasks import adding_task
from django.http import HttpResponse
from django.core import serializers
from django.http.response import JsonResponse
from celery.result import AsyncResult



# Create your views here.

def celeryAdd():
    result=adding_task.apply_async((69,2),countdown=3)
    celery_task=Tasks(primaryid=result.task_id,status=result.status)
    celery_task.save()

def celeryFunction(request):

    celeryAdd()
    queryset1 = Tasks.objects.all()

    for task in queryset1:
        task.status=AsyncResult(task.primaryid).state
        task.save()




    queryset = Tasks.objects.all()

    serialized_queryset = serializers.serialize('python',queryset)
    return JsonResponse(serialized_queryset, safe=False)
