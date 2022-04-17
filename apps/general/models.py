from django.db import models

from apps.common.models import UUIDModel


class MilitarySpecialization(UUIDModel):
    name = models.CharField(max_length=255)
    identifier = models.IntegerField()

    def __str__(self):
        return self.name


class MilitaryRank(UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TariffCategory(UUIDModel):
    identifier = models.CharField(max_length=255)

    def __str__(self):
        return str(self.identifier)


class TariffGrid(UUIDModel):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    tariff_category = models.ForeignKey(TariffCategory, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f"Тариф для {self.position}, {self.tariff_category} розряду: {self.salary}"


class PremiumGrid(UUIDModel):
    tariff_category = models.ForeignKey(TariffCategory, on_delete=models.CASCADE)
    premium = models.PositiveIntegerField()

    def __str__(self):
        return f"Премія {self.tariff_category} розряду: {self.premium}"


class WacationType(UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PaymentType(UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
