from django.db import models
from django.core.exceptions import ValidationError
from circular_counter_app.helpers import CircularCounter

class CircularCounterField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        if isinstance(value, str):
            try:
                start, cycle_len, counter_value = map(int, value.split(':'))
                return CircularCounter(start=start, cycle_len=cycle_len, value=counter_value)
            except (ValueError, IndexError):
                raise ValidationError("Invalid CircularCounter value")
        return value

    def to_python(self, value):
        if isinstance(value, CircularCounter):
            return value
        if value is None:
            return None
        if isinstance(value, str):
            try:
                start, cycle_len, counter_value = map(int, value.split(':'))
                return CircularCounter(start=start, cycle_len=cycle_len, value=counter_value)
            except (ValueError, IndexError):
                raise ValidationError("Invalid CircularCounter value")
        return value

    def get_prep_value(self, value):
        if value is None:
            return None
        if isinstance(value, CircularCounter):
            return f"{value.start}:{value.cycle_len}:{value.value}"
        return value
