from django.db import models
from django.core.exceptions import ValidationError

class IntegerListField(models.IntegerField):
    description = "A field to store a list of integers"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', [])
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs

    # def get_internal_type(self):
    #     return 'CharField'

    # def to_python(self, value):
    #     if isinstance(value, list):
    #         return value
    #     elif value is None:
    #         return []
    #     else:
    #         try:
    #             return [int(x) for x in value.split(',')]
    #         except (ValueError, TypeError):
    #             raise ValidationError("Invalid input for IntegerListField")

    # def from_db_value(self, value, expression, connection):
    #     return self.to_python(value)

    # def get_db_prep_value(self, value, connection, prepared=False):
    #     return ','.join(str(x) for x in value)
