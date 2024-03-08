from django.urls import path
from . import views

urlpatterns = [
    path('sendmail/', views.send_mail_to_all, name="sendmail"),
    path('schedule_mail/', views.schedule_mail, name="schedule_mail"),
]
