from re import S
from django.db import models
from apps.common.models import StreetAddress, UUIDModel

from apps.general.models import MilitaryRank, MilitarySpecialization, Position, TariffGrid


class MilitaryUnit(UUIDModel):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(
        StreetAddress,
        on_delete=models.CASCADE,
        related_name='military_units'
    )

    def __str__(self):
        return self.name


class Person(UUIDModel):
    class GenderChoices(models.Choices):
        MALE = 'M'
        FEMALE = 'F'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=3, choices=GenderChoices.choices)
    birth_date = models.DateField()

    address = models.ForeignKey(
        StreetAddress,
        on_delete=models.CASCADE,
        related_name='persons'
    )
    family_status = models.CharField(max_length=255)
    children_number = models.PositiveIntegerField()

    phone_number = models.CharField(max_length=20)

    tin = models.CharField(max_length=15)

    recruitment_office = models.ForeignKey(
        MilitaryUnit,
        on_delete=models.CASCADE,
        related_name='recruitment_persons'
    )
    military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.CASCADE,
        related_name='persons'
    )
    military_specialization = models.ForeignKey(
        MilitarySpecialization,
        on_delete=models.CASCADE,
        related_name='persons'
    )
    length_of_service = models.PositiveIntegerField()
    contract_term = models.PositiveIntegerField()

    @property
    def full_name(self):
        return f'{self.last_name} {self.middle_name} {self.first_name}'

    def __str__(self):
        return f'{self.full_name} ({self.military_rank})'


class Staff(UUIDModel):
    military_unit = models.ForeignKey(
        MilitaryUnit,
        on_delete=models.CASCADE,
        related_name='staff'
    )
    tariff = models.ForeignKey(
        TariffGrid,
        on_delete=models.CASCADE,
        related_name='military_unit_staff'
    )
    inner_military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.CASCADE,
        related_name='military_unit_staff'
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='staff_role'
    )

    def __str__(self):
        return f'{self.full_name} ({self.staff_military_rank}) з {self.military_unit.name}'

