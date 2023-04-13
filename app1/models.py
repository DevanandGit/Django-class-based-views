from django.db import models

class class4Model(models.Model):
    name = models.CharField(max_length=300)
    roll_no = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name} is {self.roll_no}"