import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


# Choices
class FamilyStatusTypes(models.TextChoices):
    MARRIED_MAN = "одружений", "одружений"
    NOT_MARRIED_MAN = "неодружений", "неодружений"
    MARRIED_WOMAN = "заміжня", "заміжня"
    NOT_MARRIED_WOMAN = "незаміжня", "незаміжня"
    DIVORCED_MAN = "розлучений", "розлучений"
    DIVORCED_WOMAN = "розлучена", "розлучена"
    WIDOW = "вдова", "вдова"
    WIDOWER = "вдівець", "вдівець"


class UUIDModel(models.Model):
    """
    Base abstract model that provides 'uuid' primary key field to replace the default PK
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = _('UUID Model')
        verbose_name_plural = _('UUID Models')
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


class TimeStamp(models.Model):
    """
    Represents a basic model which store information about time
    """

    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True, editable=False, null=True)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True, editable=False, null=True)

    class Meta:
        abstract = True
