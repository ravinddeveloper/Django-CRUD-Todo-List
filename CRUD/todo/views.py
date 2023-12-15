from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def crud(request):
    t_list=To_do_list.objects.all().order_by('-date_of_posted').order_by('completed')
    if request.method=='POST':  
        text=request.POST.get('text')
        due=request.POST.get('d_date')
        t=To_do_list.objects.create(text=text,due_date=due)
    return render(request,"index.html",{'list':t_list})

def t_delete(request,id):
    t_list=To_do_list.objects.get(id=id).delete()
    return redirect('/')
    
def t_complete(request,id):
    t_list=To_do_list.objects.get(id=id)
    t_list.completed=True
    t_list.save()
    return redirect('/')