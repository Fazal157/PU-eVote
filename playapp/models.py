from django.db import models

class Student(models.Model):
    email = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=50)
    roll = models.CharField(max_length=20, unique=True)  # <-- ADD THIS
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fullname
    
 



