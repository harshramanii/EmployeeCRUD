from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee


# Create your views here.


def DisplayEmployeeData(request):
    allEmployee = Employee.objects.all()
    return render(request, 'EmployeeApp/DisplayEmployeeData.html', context={'as': allEmployee})


def AddEmployee(request):
    return render(request, 'EmployeeApp/AddEmployee.html')


def SignUp(request):
    return render(request, 'EmployeeApp/SignUp.html')


def UpdateEmployee(request, sid):
    allEmployee = Employee.objects.all()
    allEmployee = Employee.objects.filter(id=sid)

    return render(request, 'EmployeeApp/UpdateEmployee.html', context={'as': allEmployee})


def InsertEmployeeRecord(request):
    name = request.GET['name']
    email = request.GET['email']
    state = request.GET['state']
    department = request.GET['department']
    s = Employee(name=name, email=email, state=state, department=department)
    s.save()
    return HttpResponse(DisplayEmployeeData(request))


def UpdateEmployeeRecord(request, eid):
    name = request.GET['name']
    email = request.GET['email']
    state = request.GET['state']
    department = request.GET['department']
    s = Employee(id=eid, name=name, email=email,
                 state=state, department=department)
    s.save()
    return HttpResponse(DisplayEmployeeData(request))


def DeleteEmployeeRecord(request, sid):
    s = Employee.objects.filter(id=sid)
    s.delete()
    return HttpResponse(DisplayEmployeeData(request))
