from django.urls import path
from . import views 
from .views import (EmployeeListView,
                     EmployeeDetailView, 
                     EmployeeCreateView,
                     EmployeeUpdateView,
                     EmployeeDeleteView)


urlpatterns = [
    path('', EmployeeListView.as_view() , name='home'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name="employee_detail"),
    path('employee/add/', EmployeeCreateView.as_view(), name="add_employee"),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name="update_employee"),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name="delete_employee"),

]
