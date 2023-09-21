from django.db import models
from .custom_fields import IntegerListField
# Create your models here.

class MyModel(models.Model):
    integer_list =IntegerListField()
