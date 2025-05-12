from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Ensure this line doesn't have parentheses
