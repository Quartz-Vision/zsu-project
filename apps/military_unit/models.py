from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import StreetAddress, UUIDModel
from apps.general.models import MilitaryRank, MilitarySpecialization, TariffGrid


class MilitaryUnit(UUIDModel):
    class Meta:
        verbose_name = _('Military Unit')
        verbose_name_plural = _('Military Units')

    name = models.CharField(max_length=255)
    address = models.ForeignKey(
        StreetAddress,
        on_delete=models.CASCADE,
        related_name='military_units'
    )

    def __str__(self):
        return self.name


class Person(UUIDModel):
    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    class GenderChoices(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    first_name = models.CharField(max_length=255, verbose_name=_('First name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last name'))
    middle_name = models.CharField(max_length=255, verbose_name=_('Middle name'))
    gender = models.CharField(max_length=3, choices=GenderChoices.choices, verbose_name=_('Gender'))
    birth_date = models.DateField(verbose_name=_('Birth date'))

    address = models.ForeignKey(
        StreetAddress,
        on_delete=models.CASCADE,
        related_name='persons',
        verbose_name=_('Address')
    )
    family_status = models.CharField(max_length=255, verbose_name=_('Family status'))
    children_number = models.PositiveIntegerField(verbose_name=_('Children number'))

    phone_number = models.CharField(max_length=20, verbose_name=_('Phone number'))

    tin = models.CharField(max_length=15, verbose_name=_('TIN'))

    recruitment_office = models.ForeignKey(
        MilitaryUnit,
        on_delete=models.CASCADE,
        related_name='recruitment_persons',
        verbose_name=_('Recruitment office')
    )
    military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.CASCADE,
        related_name='persons',
        verbose_name=_('Military rank')
    )
    military_specialization = models.ForeignKey(
        MilitarySpecialization,
        on_delete=models.CASCADE,
        related_name='persons',
        verbose_name=_('Military specialization')
    )
    length_of_service = models.PositiveIntegerField(verbose_name=_('Length of service'))
    contract_term = models.PositiveIntegerField(verbose_name=_('Contract term'))

    @property
    def full_name(self):
        return f'{self.last_name} {self.middle_name} {self.first_name}'

    def __str__(self):
        return f'{self.full_name} ({self.military_rank})'


class Staff(UUIDModel):
    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')

    military_unit = models.ForeignKey(
        MilitaryUnit,
        on_delete=models.CASCADE,
        related_name='staff',
        verbose_name=_('Military unit')
    )
    tariff = models.ForeignKey(
        TariffGrid,
        on_delete=models.CASCADE,
        related_name='military_unit_staff',
        verbose_name=_('Tariff')
    )
    inner_military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.CASCADE,
        related_name='military_unit_staff',
        verbose_name=_('Inner military rank')
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='staff_role',
        verbose_name=_('Person')
    )

    def __str__(self):
        return f'{self.person.full_name} ({self.inner_military_rank}) з {self.military_unit.name}'
