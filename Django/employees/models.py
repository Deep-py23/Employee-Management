from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}-{self.location}"


class Employee(models.Model):

    DESIGNATION_CHOICES = [
    ("HR", "HR"),
    ("SE", "Software Engineer"),
    ("SD", "Software Developer"),
    ("QA", "QA Engineer"),
    ("PM", "Project Manager"),
    ("INTERN", "Intern"),
     ]
    image = models.ImageField(upload_to='emp_images', default='emp_images/Default.png')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=10, choices=DESIGNATION_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=12)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, 
                                   blank=True, null=True)
    manager = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL,
                                 null=True, blank=True, 
                                 related_name='employee')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"