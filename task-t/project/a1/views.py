from django.shortcuts import render,redirect
from .models import IOT

# Create your views here.
def index(request):
    data=IOT.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def insertData(request):
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        print(id,name)
        query=IOT(uid=id,name=name)
        query.save()
        return redirect("/")

    return render(request,"index.html")
def updateData(request,uid):
    if request.method=="POST":
        id=request.POST['id']
        name=request.POST['name']
        edit = IOT.objects.get(uid=uid)
        edit.name=name
        edit.save()
        return redirect("/")
    d=IOT.objects.get(uid=uid)
    context={"d":d}
    return render(request,"edit.html",context)
def deleteData(request,uid):
    d = IOT.objects.get(uid=uid)
    d.delete()
    return redirect("/")
def about(request):
    return render(request,"about.html")

