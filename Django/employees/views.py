from django.views.generic import (ListView, 
                                  DeleteView,
                                  DetailView, 
                                  UpdateView, 
                                  CreateView)

from . models import Employee
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q


class EmployeeListView(PermissionRequiredMixin, ListView):
    permission_required = 'employees.view_employee'
    model = Employee
    template_name = 'home.html'
    context_object_name = 'employees'


    def get_queryset(self):
        qs = Employee.objects.select_related('department', 'manager')
        user = self.request.user
        if user.has_perm('employees.change_employee'):
            return qs
        return qs.filter(Q(user=user) | Q(manager__user = user))
            

class EmployeeDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'employees.view_employee'
    model = Employee
    template_name = 'employee_detail.html'

    def get_queryset(self):
        qs = Employee.objects.select_related('department', 'manager')
        user = self.request.user
        if user.has_perms('employees.change_employee'):
            return qs
        return qs.filter(Q(user=user) | Q(manager__user = user))



class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'employees.add_employee'
    model = Employee
    template_name = 'add_update_employee.html'
    fields = ['first_name', 'last_name', 'designation', 'salary', 'is_active', 'phone_number', 'email', 'manager', 'user', 'department']
    success_url = reverse_lazy('home')


class EmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'employees.change_employee'
    model = Employee
    template_name = 'add_update_employee.html'
    fields = ['first_name', 'last_name', 'designation', 'salary', 'is_active', 'phone_number', 'email', 'manager', 'user', 'department']

    def get_success_url(self):
        return reverse('employee_detail', kwargs={'pk': self.object.pk})

   
class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'employees.delete_employee'
    model = Employee
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('home')