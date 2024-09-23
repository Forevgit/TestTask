from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    doctor = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='doctor_for_patient'
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name
