from django.shortcuts import render
from job.models import Job
from django.core.paginator import Paginator
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'job/job_list.html',context={'jobs':page_obj})




def job_details(request, slug):
    jobs_details = Job.objects.get(slug=slug)
    return render(request, 'job/job_detail.html',context={'jobs_details':jobs_details})