from django.urls import path
from . views import job_list,job_details 

app_name='job'

urlpatterns = [
    path('',job_list),
    path('<str:slug>',job_details,name='job_detail')
]
