from operator import mod
from statistics import mode
from turtle import position
from django.db import models


class MilitarySpecialization(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.IntegerField()

    def __str__(self):
        return self.name


class MilitaryRank(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TariffCategory(models.Model):
    identifier = models.CharField(max_length=255)

    def __str__(self):
        return str(self.identifier)


class TariffGrid(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    tariff_category = models.ForeignKey(TariffCategory, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f"Тариф для {self.position}, {self.tariff_category} розряду: {self.salary}"


class PremiumGrid(models.Model):
    tariff_category = models.ForeignKey(TariffCategory, on_delete=models.CASCADE)
    premium = models.PositiveIntegerField()

    def __str__(self):
        return f"Премія {self.tariff_category} розряду: {self.premium}"


class WacationType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
