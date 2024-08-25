from django.core import checks
from django.db import models


class OrderField(models.PositiveIntegerField):
    description = "Ordering field on a unique field"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_unique_for_field(**kwargs),
        ]

    def _check_unique_for_field(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error(
                    "OrderField must define a unique_for_field.",
                    obj=self,
                    id="fields.E300",
                )
            ]
        elif self.unique_for_field not in [
            f.name for f in self.model._meta.get_fields()
        ]:
            return [
                checks.Error(
                    "OrderField has an invalid value for unique_for_field.",
                    obj=self,
                    id="fields.E301",
                )
            ]
        return []
