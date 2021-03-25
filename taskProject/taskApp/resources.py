from tastypie.resources import ModelResource
from taskApp.models import Tasks
from tastypie.authorization import Authorization
from taskApp.tasks import adding_task

def celeryAdd():
    result=adding_task.apply_async((2,2),countdown=3)
    celery_task=Tasks(primaryid=result.task_id,status=result.status)
    celery_task.save()


class TasksResource(ModelResource):
    class Meta:
        queryset = Tasks.objects.all()
        resource_name = 'tasks'
        authorization = Authorization()
