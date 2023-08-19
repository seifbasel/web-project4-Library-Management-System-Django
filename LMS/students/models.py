from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=8,default=1234)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    birthdate = models.DateField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    @classmethod
    def get_all_students(cls):
        return cls.objects.all()
