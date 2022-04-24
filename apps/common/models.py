import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDModel(models.Model):
    """
    Base abstract model that provides 'uuid' primary key field to replace the default PK
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'<{self.__class__.__name__} {self.id}>'


class City(UUIDModel):
    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class StreetAddress(UUIDModel):
    class Meta:
        verbose_name = _('Street Address')
        verbose_name_plural = _('Street Addresses')

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='street_addresses',
        verbose_name=_('City')
    )

    name = models.CharField(max_length=255, verbose_name=_('Street name'))

    def __str__(self):
        return f'{self.city}, {self.name}'