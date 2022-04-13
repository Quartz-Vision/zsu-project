from django.db import models

from apps.general.models import MilitaryRank, MilitarySpecialization, Position, TariffGrid


class MilitaryUnit(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Staff(models.Model):
    military_unit = models.ForeignKey(
        MilitaryUnit,
        on_delete=models.CASCADE,
        related_name='staff'
    )
    tarif = models.ForeignKey(
        TariffGrid,
        on_delete=models.CASCADE,
        related_name='military_unit_staff'
    )
    military_specialization = models.ForeignKey(
        MilitarySpecialization,
        on_delete=models.CASCADE,
        related_name='military_unit_staff'
    )
    staff_military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.CASCADE,
        related_name='military_unit_inner_staff'
    )
    military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.CASCADE,
        related_name='military_unit_staff'
    )
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} ({self.staff_military_rank}) з {self.military_unit.name}"
