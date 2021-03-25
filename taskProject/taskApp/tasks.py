from celery import shared_task

from taskApp.models import Tasks


@shared_task
def adding_task(x, y):


    return x+y
