from django.db import models

from apps.common.models import UUIDModel
from django.utils.translation import gettext_lazy as _


class MilitarySpecialization(UUIDModel):
    class Meta:
        verbose_name = _('Military Specialization')
        verbose_name_plural = _('Military Specializations')

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    identifier = models.IntegerField(verbose_name=_('Identifier'))

    def __str__(self):
        return self.name


class MilitaryRank(UUIDModel):
    class Meta:
        verbose_name = _('Military Rank')
        verbose_name_plural = _('Military Ranks')

    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class PremiumGrid(UUIDModel):
    class Meta:
        verbose_name = _('Premium Grid')
        verbose_name_plural = _('Premium Grid')

    premium = models.PositiveIntegerField(verbose_name=_('Premium'))

    def __str__(self):
        return f"Премія: {self.premium}"


class TariffCategory(UUIDModel):
    class Meta:
        verbose_name = _('Tariff Category')
        verbose_name_plural = _('Tariff Categories')

    premium_grid = models.ForeignKey(
        PremiumGrid,
        on_delete=models.CASCADE,
        verbose_name=_('Premium Grid'),
        related_name="tariff_category",
        null=True,
    )
    identifier = models.CharField(max_length=255, verbose_name=_('Identifier'))

    def __str__(self):
        return str(self.identifier)


class TariffGrid(UUIDModel):
    class Meta:
        verbose_name = _('Tariff Grid')
        verbose_name_plural = _('Tariff Grid')

    tariff_category = models.ForeignKey(TariffCategory, on_delete=models.CASCADE, verbose_name=_('Tariff Category'))
    salary = models.PositiveIntegerField(verbose_name=_('Salary'))

    def __str__(self):
        return f"Тариф для {self.position}, {self.tariff_category} розряду: {self.salary}"


class Position(UUIDModel):
    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    tariff = models.ForeignKey(
        TariffGrid,
        on_delete=models.CASCADE,
        verbose_name=_('Tariff Grid'),
        related_name="position",
        null=True,
    )

    def __str__(self):
        return self.name


class WacationType(UUIDModel):
    class Meta:
        verbose_name = _('Wacation Type')
        verbose_name_plural = _('Wacation Types')

    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class PaymentType(UUIDModel):
    class Meta:
        verbose_name = _('Payment Type')
        verbose_name_plural = _('Payment Types')

    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class ReasonType(UUIDModel):
    class Meta:
        verbose_name = _('Reason Type')
        verbose_name_plural = _('Reason Types')

    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name
