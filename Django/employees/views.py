from django.shortcuts import render, get_object_or_404, redirect
from . models import Employee
from . forms import EmployeeForm
from django.contrib.auth.decorators import login_required




def employee_detail(request, pk):
    employee = get_object_or_404 (Employee, pk=pk)
    return render(request, "employee_detail.html", {'employee':employee})


@login_required
def add_employee(request):
    if request.method=='POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request,"add_update_employee.html", {'form': form})


@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'add_update_employee.html', {'form':form, 'employee':employee} )



def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method=='POST':
        employee.delete()
        return redirect('home')

    return render(request, 'delete_confirm.html', {'employee':employee})














