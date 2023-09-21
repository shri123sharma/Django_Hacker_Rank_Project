from django.db import models
from circular_counter_app.fields import CircularCounterField
# Create your models here.

class State(models.Model):
    counter = CircularCounterField()
    
    