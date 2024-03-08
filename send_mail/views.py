from django.shortcuts import render
from django.http import HttpResponse
from send_mail.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# Create your views here.


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=18, minute=50)
    task = PeriodicTask.objects.create(
        crontab=schedule, name="schedule_mail_task_"+"4", task='send_mail.tasks.send_mail_func')  # , args=json.dumps(([[2, 3]])))
    return HttpResponse("Done")
