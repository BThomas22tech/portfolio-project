from django.shortcuts import render, get_object_or_404
from .models import Job
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})

def detail(request,job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html',{'job':job_detail})

def external_URL():
    external_URL = Job.urls
    return redirect(external_URL)
    