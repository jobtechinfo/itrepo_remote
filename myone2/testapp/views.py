from django.shortcuts import render,redirect
from testapp.models import jobs
from testapp.forms import jobsform,hydjobsform,bngljobsform,signup_form
from django.http import HttpResponse
from testapp.models import hydjobs,bngljobs
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def jobs_info_view(request):
    softjobs=jobs.objects.all()

    return render(request,'testapp/list.html',{'softjobs':softjobs})
def jobs_list_view(request):
    return render(request,'testapp/index.html')
def jobs_update_info(request):
    myform=jobsform()
    if request.method=="POST":
        myform1=jobsform(request.POST)
        if myform1.is_valid():
            myform1.save(commit=True)
            return render(request,'testapp/wish.html')
    return render(request,'testapp/update.html',{'myform':myform})
@login_required
def delete_jobs_view(request,id):
    cmpdelete=jobs.objects.get(id=id)
    if request.method=="POST":
        cmpdelete.delete()
        return redirect("/jobs")
    return render(request,'testapp/delete.html',{'cmpdelete':cmpdelete})
@login_required
def hyd_jobs_view(request):
    softjobs=hydjobs.objects.all()
    return render(request,'testapp/list1.html',{'softjobs':softjobs})
def hyd_jobs_update(request):
    myform=hydjobsform()
    if request.method=="POST":
        myform1=hydjobsform(request.POST)
        if myform1.is_valid():
            myform1.save(commit=True)
            return render(request,'testapp/wish.html')
    return render(request,'testapp/update1.html',{'myform':myform})


def hyd_delete_view(request,id):
    cmpdelete=hydjobs.objects.get(id=id)
    if request.method=="POST":
        cmpdelete.delete()
        return redirect("/hydjobs")
    return render(request,'testapp/hyd_delete.html',{'cmpdelete':cmpdelete})
@login_required
def bngl_jobs_view(request):
    softjobs=bngljobs.objects.all()
    return render(request,'testapp/list2.html',{'softjobs':softjobs})

def bngl_jobs_update(request):
    myform=bngljobsform()
    if request.method=="POST":
        myform1=bngljobsform(request.POST)
        if myform1.is_valid():
            myform1.save(commit=True)
            return render(request,'testapp/wish.html')
    return render(request,'testapp/update2.html',{'myform':myform})

def bngl_delete_view(request,id):
    cmpdelete=bngljobs.objects.get(id=id)
    if request.method=="POST":
        cmpdelete.delete()
        return redirect("/bngljobs")
    return render(request,'testapp/bngl_delete.html',{'cmpdelete':cmpdelete})

def logout_view(request):
    if request.method=="POST":
        return redirect('/index')
    return render(request,'testapp/logout.html')

def signup_view(request):
    myform=signup_form()
    if request.method=="POST":
        form=signup_form(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')
    return render(request,'testapp/signup.html',{"myform":myform})
