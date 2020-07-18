from django.shortcuts import render,redirect
from django.contrib import messages
from app4.models import Schedule_New_course
from app4.models import StudentModel
def ShowIndex(request):
    return render(request, "adminlogin.html")
def Admin_check(request):
    na=request.POST.get("t1")
    pa=request.POST.get("t2")
    if na=="krishna" and pa=="Krish7":
        return render(request,"welcome.html")
    else:
        return render(request,"adminlogin.html",{"message":"InvalidUser"})
def Home(request):
    return render(request,"welcome.html")
def scheduleNewCourse(request):
    return render(request,"schedule_new_course.html" )
def register(request):
    co=request.POST.get("t1")
    fa=request.POST.get("t2")
    da=request.POST.get("t3")
    ti=request.POST.get("t4")
    fee=request.POST.get("t5")
    du=request.POST.get("t6")
    sc=Schedule_New_course(course=co,faculty=fa,date=da,time=ti,fee=fee,duration=du)
    sc.save()
    return redirect(scheduleNewCourse)
def ViewClasses(request):
    results=Schedule_New_course.objects.all()
    return render(request,"viewclasses.html",{"data":results})
def Student(request):
    return render(request,"student.html")
def StudentRegister(request):
    return render(request,"register.html")
def RegisterStudent(request):
    na=request.POST.get("t1")
    co=request.POST.get("t2")
    em=request.POST.get("t3")
    pa=request.POST.get("t4")
    sm=StudentModel(name=na,contactno=co,email=em,password=pa)
    sm.save()
    return redirect('student_register')
def LoginCheck(request):
    return render(request,"login.html")

def AfterLogin(request):
    return render(request,"afterlogin.html")



