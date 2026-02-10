from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def home(request):
    employees=Employee.objects.all()

    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EmployeeForm()

    return render(request,'employee_home.html',{
        'form':form,
        'employees':employees
    })


#READ 
def read_employee(request, id):
    employee=get_object_or_404(Employee, id=id)
    return render(request,'read_employee.html',{
        'employee':employee
    })


#UPDATE
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method=="POST":
        form=EmployeeForm(request.POST, nstance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EmployeeForm(instance=employee)

    return render(request,'update_employee.html',{
        'form':form
    })


# DELETE
def delete_employee(request, id):
    employee=get_object_or_404(Employee, id=id)

    if request.method=="POST":
        employee.delete()
        return redirect('home')

    return render(request,'delete_employee.html',{
        'employee':employee
    })







# Create your views here.
