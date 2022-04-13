import uuid

from django.db import models


class UUIDModel(models.Model):
    """
    Base abstract model that provides 'uuid' primary key field to replace the default PK
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'<{self.__class__.__name__} {self.id}>'
