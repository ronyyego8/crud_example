from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except Exception as e:                
                print(e)
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("/show")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {'employee': employee, 'form': form})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
