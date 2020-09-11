from django.db import models

class Member(models.Model):
    name=models.TextField(null=False)
    birth_date=models.DateField()

